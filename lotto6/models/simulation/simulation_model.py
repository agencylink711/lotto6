"""SimulationModel for storing lottery simulation results and configurations."""

from datetime import datetime
from typing import Optional, Dict, Any, List
from sqlmodel import SQLModel, Field, JSON, Column, ForeignKey, String


class SimulationModel(SQLModel, table=True):
    """
    Model for storing lottery simulation results and configurations.
    
    Supports both temporary simulations (in-memory/session) and saved simulations
    (persistent database storage). Follows the same patterns as AnalysisModel
    for consistency and maintainability.
    
    Table Name: simulation_model
    
    Access Control:
    - Regular Users: Maximum 1 saved simulation (replace on new save)
    - Admin Users: Unlimited saved simulations
    - Anonymous Users: Temporary simulations only (no save capability)
    """
    
    __tablename__ = "simulation_model"
    
    # Primary key
    id: Optional[int] = Field(primary_key=True, default=None)
    
    # Foreign key to User model via clerk_user_id
    user_clerk_id: str = Field(
        sa_column=Column(String(255), ForeignKey("user.clerk_user_id")),
        description="Clerk user ID from User model"
    )
    
    # Simulation configuration
    simulation_type: str = Field(
        max_length=50,
        description="Type of simulation: random, frequency_based, overdue_based, mixed_strategy, monte_carlo"
    )
    
    simulation_name: str = Field(
        max_length=200,
        description="User-defined name for the simulation"
    )
    
    # JSON fields for flexible data storage
    parameters: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        description="Simulation configuration parameters (number_of_simulations, weights, etc.)"
    )
    
    results_json: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        description="Generated simulation results with Sim_1, Sim_2, etc. format"
    )
    
    execution_metadata: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        description="Execution statistics and performance data",
        alias="metadata"
    )
    
    # Access control flags
    is_admin_simulation: bool = Field(
        default=False,
        description="Whether this is an admin-created simulation"
    )
    
    is_public: bool = Field(
        default=False,
        description="Whether the simulation is publicly viewable"
    )
    
    # Timestamps
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When the simulation was created"
    )
    
    updated_at: Optional[datetime] = Field(
        default=None,
        description="When the simulation was last updated"
    )
    
    def __repr__(self) -> str:
        """String representation of the simulation model."""
        return (
            f"SimulationModel(id={self.id}, "
            f"user_clerk_id='{self.user_clerk_id}', "
            f"simulation_type='{self.simulation_type}', "
            f"simulation_name='{self.simulation_name}')"
        )
    
    def can_user_access(self, user_clerk_id: str, is_admin: bool = False) -> bool:
        """
        Check if a user can access this simulation.
        
        Args:
            user_clerk_id: The Clerk user ID to check access for
            is_admin: Whether the user has admin privileges
            
        Returns:
            bool: True if the user can access this simulation
        """
        # Admin users can access all simulations
        if is_admin:
            return True
        
        # Public simulations can be accessed by anyone
        if self.is_public:
            return True
        
        # Users can only access their own simulations
        return self.user_clerk_id == user_clerk_id
    
    def get_simulation_count(self) -> int:
        """
        Get the number of simulations in the results.
        
        Returns:
            int: Number of simulations generated
        """
        if not self.results_json or "simulations" not in self.results_json:
            return 0
        
        simulations = self.results_json["simulations"]
        if isinstance(simulations, dict):
            return len(simulations)
        elif isinstance(simulations, list):
            return len(simulations)
        
        return 0
    
    def get_simulation_results_display(self) -> List[str]:
        """
        Get simulation results in display format: ["Sim_1: [1, 2, 3, 4, 5, 6]", ...]
        
        Returns:
            List[str]: Formatted simulation results for display
        """
        if not self.results_json or "simulations" not in self.results_json:
            return []
        
        simulations = self.results_json["simulations"]
        if not isinstance(simulations, dict):
            return []
        
        display_results = []
        for sim_id, numbers in simulations.items():
            if isinstance(numbers, list):
                numbers_str = str(numbers).replace("'", "")  # Remove quotes if any
                display_results.append(f"{sim_id}: {numbers_str}")
        
        return display_results
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """
        Get summary statistics from the simulation results.
        
        Returns:
            Dict[str, Any]: Summary statistics or empty dict if not available
        """
        if not self.results_json:
            return {}
        
        return self.results_json.get("summary_statistics", {})
    
    def get_execution_info(self) -> Dict[str, Any]:
        """
        Get execution information from the simulation results.
        
        Returns:
            Dict[str, Any]: Execution info or empty dict if not available
        """
        if not self.results_json:
            return {}
        
        return self.results_json.get("execution_info", {})
    
    def get_analysis_base_data(self) -> Dict[str, Any]:
        """
        Get analysis base data used for the simulation (if applicable).
        
        Returns:
            Dict[str, Any]: Analysis base data or empty dict if not available
        """
        if not self.results_json:
            return {}
        
        return self.results_json.get("analysis_base_data", {})
    
    def update_metadata_on_save(self) -> None:
        """Update execution metadata when the simulation is saved."""
        self.updated_at = datetime.utcnow()
        
        if not self.execution_metadata:
            self.execution_metadata = {}
        
        self.execution_metadata.update({
            "last_saved_at": self.updated_at.isoformat(),
            "simulation_count": self.get_simulation_count(),
            "has_results": bool(self.results_json and "simulations" in self.results_json)
        })
    
    @classmethod
    def create_simulation_result(
        cls,
        simulation_type: str,
        user_input: Dict[str, Any],
        simulations: Dict[str, List[int]],
        summary_statistics: Dict[str, Any],
        execution_info: Optional[Dict[str, Any]] = None,
        analysis_base_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a standardized simulation result structure.
        
        Args:
            simulation_type: Type of simulation performed
            user_input: Original user input parameters
            simulations: Dictionary of simulation results {"Sim_1": [1,2,3,4,5,6], ...}
            summary_statistics: Statistical analysis of results
            execution_info: Optional execution metadata
            analysis_base_data: Optional base analysis data used
            
        Returns:
            Dict[str, Any]: Standardized simulation result structure
        """
        result = {
            "simulation_type": simulation_type,
            "user_input": user_input,
            "simulations": simulations,
            "summary_statistics": summary_statistics
        }
        
        if execution_info:
            result["execution_info"] = execution_info
        
        if analysis_base_data:
            result["analysis_base_data"] = analysis_base_data
        
        return result
    
    @classmethod
    def validate_simulation_parameters(cls, simulation_type: str, parameters: Dict[str, Any]) -> bool:
        """
        Validate simulation parameters based on simulation type.
        
        Args:
            simulation_type: Type of simulation
            parameters: Parameters to validate
            
        Returns:
            bool: True if parameters are valid
        """
        if not isinstance(parameters, dict):
            return False
        
        # Common required parameters
        if "number_of_simulations" not in parameters:
            return False
        
        num_simulations = parameters["number_of_simulations"]
        if not isinstance(num_simulations, int) or num_simulations < 1 or num_simulations > 500:
            return False
        
        # Type-specific validation
        if simulation_type == "frequency_based":
            required_fields = ["number_of_past_draws", "strategy"]
            return all(field in parameters for field in required_fields)
        
        elif simulation_type == "overdue_based":
            required_fields = ["minimum_days_overdue", "number_of_past_draws"]
            return all(field in parameters for field in required_fields)
        
        elif simulation_type == "mixed_strategy":
            required_fields = ["number_of_past_draws", "strategy_weights"]
            if not all(field in parameters for field in required_fields):
                return False
            
            # Validate strategy weights
            weights = parameters["strategy_weights"]
            if not isinstance(weights, dict):
                return False
            
            # Check if weights sum to approximately 1.0
            total_weight = sum(weights.values())
            return 0.95 <= total_weight <= 1.05
        
        elif simulation_type == "monte_carlo":
            required_fields = ["iterations", "strategy_distribution"]
            if not all(field in parameters for field in required_fields):
                return False
            
            # Validate strategy distribution
            distribution = parameters["strategy_distribution"]
            if not isinstance(distribution, dict):
                return False
            
            # Check if distribution sums to approximately 1.0
            total_distribution = sum(distribution.values())
            return 0.95 <= total_distribution <= 1.05
        
        # For random simulations, basic validation is sufficient
        return True
