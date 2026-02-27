from pydantic import BaseModel, Field
from typing import Annotated

class predictionResponse(BaseModel):

  bmi: Annotated[float, Field(..., description="Bmi of User", examples=[24.00])]
  age_group: Annotated[str, Field(..., description="Age group of User", examples=["middle_aged"])]
  lifestyle_risk: Annotated[bool, Field(..., description="lifestyle_risk of User", examples=[True])]
  city_tier: Annotated[str, Field(..., description="City of User", examples=["Delhi"])]
  income_lpa: Annotated[float, Field(..., description="income_lpa of User", examples=[5.5])]
  occupation: Annotated[str, Field(..., description="occupation of User", examples=["Students"])]

  predicted_category: Annotated[str, Field(..., description="predicted_category of User", examples=["High"])]
