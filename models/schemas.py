from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Observation(BaseModel):
    """Single observation from inspection"""
    area: str = Field(description="Location/area of observation")
    issue: str = Field(description="Description of the issue")
    severity: Literal["Good", "Moderate", "Poor", "Not Available"] = Field(description="Severity level")
    source: Literal["inspection", "thermal", "both"] = Field(description="Data source")
    details: Optional[str] = Field(default=None, description="Additional details")
    
class ThermalReading(BaseModel):
    """Thermal imaging data"""
    area: str = Field(description="Location of thermal reading")
    temperature: Optional[str] = Field(default=None, description="Temperature reading")
    finding: str = Field(description="Thermal observation")
    image_reference: Optional[str] = Field(default=None, description="Image reference")

class InspectionData(BaseModel):
    """Extracted inspection report data"""
    property_info: dict = Field(description="Property details")
    observations: List[Observation] = Field(description="List of observations")
    structural_conditions: dict = Field(description="Structural assessment")
    
class ThermalData(BaseModel):
    """Extracted thermal report data"""
    thermal_readings: List[ThermalReading] = Field(description="Thermal observations")
    
class MergedData(BaseModel):
    """Validated and merged data"""
    observations: List[Observation] = Field(description="Merged observations")
    conflicts: List[str] = Field(default_factory=list, description="Detected conflicts")
    missing_info: List[str] = Field(default_factory=list, description="Missing information")
    
class DDRReport(BaseModel):
    """Final DDR structure"""
    property_summary: str = Field(description="Property issue summary")
    area_observations: dict = Field(description="Area-wise observations")
    root_cause: str = Field(description="Probable root cause analysis")
    severity_assessment: dict = Field(description="Severity with reasoning")
    recommendations: List[str] = Field(description="Recommended actions")
    additional_notes: List[str] = Field(description="Additional notes")
    missing_information: List[str] = Field(description="Missing or unclear info")
