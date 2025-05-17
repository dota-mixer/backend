from pydantic import ConfigDict
from sqlmodel import JSON, Field, SQLModel
from typing import Optional
from enum import IntEnum


class PrimaryAttribute(IntEnum):
    STRENGTH = 0
    AGILITY = 1
    INTELLIGENCE = 2
    UNIVERSAL = 3

    @property
    def display_name(self) -> str:
        return self.name.lower()


class PositionStats(SQLModel):
    elo: Optional[int] = Field(default=None)
    matches: int = Field(default=0)
    winrate: float = Field(default=0.0, ge=0.0, le=1.0)


class HeroOut(SQLModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True
    )

    name: str = Field(alias="displayName")
    npc: str = Field(alias="npc")
    hero_id: int = Field(alias="hero_id")
    primary_attribute: PrimaryAttribute = Field(alias="primary_attribute")

    all_elo: Optional[int] = Field(alias="all elo", default=None)
    all_matches: int = Field(alias="all matches", default=0)
    all_winrate: float = Field(alias="all winrate", default=0.0)

    pos_1: PositionStats = Field(
        default_factory=PositionStats,
        alias="pos_1_stats",
        sa_column_kwargs={
            "type_": JSON(none_as_null=True).with_variant(JSON, "sqlite")
        },
    )
    pos_2: PositionStats = Field(
        default_factory=PositionStats,
        alias="pos_2_stats",
        sa_column_kwargs={
            "type_": JSON(none_as_null=True).with_variant(JSON, "sqlite")
        },
    )
    pos_3: PositionStats = Field(
        default_factory=PositionStats,
        alias="pos_3_stats",
        sa_column_kwargs={
            "type_": JSON(none_as_null=True).with_variant(JSON, "sqlite")
        },
    )
    pos_4: PositionStats = Field(
        default_factory=PositionStats,
        alias="pos_4_stats",
        sa_column_kwargs={
            "type_": JSON(none_as_null=True).with_variant(JSON, "sqlite")
        },
    )
    pos_5: PositionStats = Field(
        default_factory=PositionStats,
        alias="pos_5_stats",
        sa_column_kwargs={
            "type_": JSON(none_as_null=True).with_variant(JSON, "sqlite")
        },
    )


class HeroesOut(SQLModel):
    data: list[HeroOut]
    count: int
