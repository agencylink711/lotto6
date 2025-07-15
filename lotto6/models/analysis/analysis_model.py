"""AnalysisModel for storing lottery analysis results."""

import reflex as rx
from datetime import datetime
from sqlmodel import Field, Column, JSON
from typing import Optional, Dict, Any


class AnalysisModel(rx.Model, table=True):
    """
    Model for storing lottery analysis results.
    
    Stores analysis results, chart data, and metadata for user's lottery number analyses.
    Regular users can save 1 analysis, admin users can save unlimited analyses.
    """
    
    # Table name in snake_case following Python conventions
    __tablename__ = "analysis_model"
    
    # Primary key
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Foreign key to User model
    user_clerk_id: str = Field(
        max_length=255,
        foreign_key="user.clerk_user_id",
        index=True,
        description="Foreign key reference to User.clerk_user_id"
    )
    
    # Analysis configuration
    analysis_type: str = Field(
        max_length=50,
        index=True,
        description="Type of analysis: frequently_seen, rarely_seen, overdue, pattern"
    )
    
    analysis_name: str = Field(
        max_length=200,
        description="User-defined name for this analysis"
    )
    
    # JSON fields for flexible data storage
    parameters: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        default_factory=dict,
        description="Analysis configuration parameters (draw count, date range, etc.)"
    )
    
    results_json: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        default_factory=dict,
        description="Analysis results with English keys (top_numbers, detailed_results, metadata)"
    )
    
    chart_data: Dict[str, Any] = Field(
        sa_column=Column(JSON),
        default_factory=dict,
        description="Chart configuration and data for visualization"
    )
    
    # Access control flags
    is_admin_analysis: bool = Field(
        default=False,
        description="True if created by admin user"
    )
    
    is_public: bool = Field(
        default=False,
        index=True,
        description="True if analysis is shared publicly"
    )
    
    # Timestamps
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when analysis was created"
    )
    
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when analysis was last updated"
    )
    
    def __repr__(self) -> str:
        return f"AnalysisModel(id={self.id}, user_clerk_id='{self.user_clerk_id}', analysis_type='{self.analysis_type}', name='{self.analysis_name}')"
    
    @property
    def is_frequently_seen_analysis(self) -> bool:
        """Check if this is a frequently seen numbers analysis."""
        return self.analysis_type == "frequently_seen"
    
    @property
    def is_rarely_seen_analysis(self) -> bool:
        """Check if this is a rarely seen numbers analysis."""
        return self.analysis_type == "rarely_seen"
    
    @property
    def is_overdue_analysis(self) -> bool:
        """Check if this is an overdue numbers analysis."""
        return self.analysis_type == "overdue"
    
    @property
    def analysis_display_name(self) -> str:
        """Get the German display name for this analysis type."""
        type_mapping = {
            "frequently_seen": "Häufige Zahlen",
            "rarely_seen": "Seltene Zahlen", 
            "overdue": "Überfällige Zahlen",
            "pattern": "Muster-Analyse"
        }
        return type_mapping.get(self.analysis_type, self.analysis_type)
    
    @property
    def draws_analyzed_count(self) -> int:
        """Get the number of draws that were analyzed."""
        return self.results_json.get("metadata", {}).get("total_draws_analyzed", 0)
    
    @property
    def top_6_numbers(self) -> list[int]:
        """Get the top 6 numbers from analysis results."""
        return self.results_json.get("top_numbers", {}).get("top_6", [])
    
    @property
    def has_chart_data(self) -> bool:
        """Check if chart data is available."""
        return bool(self.chart_data and self.chart_data.get("data"))
    
    def update_timestamp(self) -> None:
        """Update the updated_at timestamp to current time."""
        self.updated_at = datetime.utcnow()
    
    @classmethod
    def create_analysis(
        cls,
        user_clerk_id: str,
        analysis_type: str,
        analysis_name: str,
        parameters: Dict[str, Any],
        results_json: Dict[str, Any],
        chart_data: Dict[str, Any],
        is_admin_analysis: bool = False,
        is_public: bool = False
    ) -> "AnalysisModel":
        """
        Factory method to create a new AnalysisModel instance.
        
        Args:
            user_clerk_id: The Clerk user ID
            analysis_type: Type of analysis (frequently_seen, rarely_seen, overdue, pattern)
            analysis_name: User-defined name for the analysis
            parameters: Analysis configuration parameters
            results_json: Analysis results data
            chart_data: Chart configuration and data
            is_admin_analysis: Whether this is an admin analysis
            is_public: Whether this analysis is public
            
        Returns:
            New AnalysisModel instance
        """
        return cls(
            user_clerk_id=user_clerk_id,
            analysis_type=analysis_type,
            analysis_name=analysis_name,
            parameters=parameters,
            results_json=results_json,
            chart_data=chart_data,
            is_admin_analysis=is_admin_analysis,
            is_public=is_public
        )
