"""Shared paths and constants for the Kikuube rehabilitation pipeline.

Import at the top of every notebook:

    import sys
    from pathlib import Path
    ROOT = next(p for p in [Path.cwd(), *Path.cwd().parents]
                if (p / "config.py").exists())
    sys.path.insert(0, str(ROOT))
    from config import *

Every path is derived from the location of this file, so the project can be
copied anywhere and run without editing.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data_raw"
OUT = ROOT / "data_derived"
FIG = ROOT / "figures"
for p in (OUT, FIG):
    p.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Raw inputs
# ---------------------------------------------------------------------------
WPDX_CSV     = RAW / "Water_Point_Data_Exchange_-_Plus_(WPdx+)_20260729-98774.csv"
CENSUS_XLSX  = RAW / "Subcounty-NPHC-2024-Profiles-Excel-Tables.xlsx"
WORLDPOP_TIF = RAW / "uga_pop_2024_CN_100m_R2025A_v1.tif"
FRICTION_TIF = RAW / "kikuube_walking_friction_2019.tif"
GHSL_TIF     = RAW / "kikuube_ghsl_smod_2020.tif"

# Boundaries.
#
# Only sub-county geometry is used, and only for the study district: 06 clips
# the population raster to it and calibrates WorldPop to the census count
# within each unit. Districts are handled by name throughout, so no district
# boundary file is read anywhere in the pipeline.
#
# COD_AB_SUBCOUNTIES_GJ is the national COD-AB adm4 layer published on HDX,
# valid 2020-08-24, the most recent sub-county geometry available from a
# citable public source. 02 subsets it to the study district and writes
# SUBCOUNTY_GJ, which every later notebook reads.
COD_AB_SUBCOUNTIES_GJ = RAW / "uga_admin4.geojson"
SUBCOUNTY_GJ          = RAW / "kikuube_subcounties_codab2020.geojson"

# ---------------------------------------------------------------------------
# Derived, written by the numbered notebooks
# ---------------------------------------------------------------------------
ANALYSIS_SAMPLE = OUT / "analysis_sample.csv"             # 01
CANDIDATES_NAT  = OUT / "candidates_national.csv"         # 01
CENSUS_HIER     = OUT / "census_hierarchy.csv"            # 02, all 147 units
SUBCOUNTY_WTS   = OUT / "kikuube_subcounty_weights.csv"   # 02, 7 units
KIKUUBE_SUPPLY  = OUT / "kikuube_supply.csv"              # 04
KIKUUBE_CAND    = OUT / "kikuube_candidates.csv"          # 04
DEMAND_CELLS    = OUT / "demand_cells.csv"                # 06
RESCALE_FACTORS = OUT / "rescale_factors.csv"             # 06
REACH_CAND      = OUT / "reach_cand.npz"                  # 07
REACH_SUPP      = OUT / "reach_supp.npz"                  # 07
SOLUTIONS       = OUT / "solutions.csv"                   # 08

DISTRICT = "Kikuube"
COUNTRY  = "Uganda"

# ---------------------------------------------------------------------------
# District names
# ---------------------------------------------------------------------------
# The water point exchange and the census tabulations spell two districts
# differently. These are variants, not boundary changes, so they are harmonised
# in 01 rather than dropped.
DISTRICT_SPELLING = {"LUWERO": "LUWEERO", "MADI OKOLLO": "MADI-OKOLLO"}

# Units whose extent changed after most water point records were collected, and
# which are therefore left out of the national comparison in 03.
#
# Ten municipalities became cities and separate local governments on 1 July
# 2020, following the parliamentary resolution of 28 April 2020 under Article
# 179(1)(A) of the Constitution; Terego and Butebo were created from Arua and
# Pallisa. Records predating those changes carry the parent's name, so parent
# and child cannot be compared on a consistent footing and both are dropped.
#
# Apaa is a disputed area, claimed by both Amuru and Adjumani. It appears at
# district level in the census with no lower units beneath it and a population
# under ten thousand. Its attribution is contested, so it is excluded rather
# than assigned to either claimant, and Amuru with it.
EXCLUDED_DISTRICTS = {
    "ARUA", "ARUA CITY", "TEREGO",
    "GULU", "GULU CITY", "OMORO",
    "HOIMA", "HOIMA CITY",
    "JINJA", "JINJA CITY",
    "LIRA", "LIRA CITY",
    "MASAKA", "MASAKA CITY",
    "MBALE", "MBALE CITY",
    "MBARARA", "MBARARA CITY",
    "SOROTI", "SOROTI CITY",
    "KABAROLE", "FORT PORTAL CITY",
    "PALLISA", "BUTEBO",
    "AMURU", "APAA",
}

# Wholly urban districts, outside the rural scope of the study. The ten cities
# created in 2020 are excluded above; Kampala is the only remaining unit with
# no rural population.
URBAN_UNITS = {"KAMPALA"}

# Sub-county units expected in the study district under COD-AB. Asserted in 02
# so that a changed input file or a mistyped filter fails immediately rather
# than propagating.
N_SUBCOUNTIES = 7

# ---------------------------------------------------------------------------
# Analysis parameters
# ---------------------------------------------------------------------------
CRS_GEO    = "EPSG:4326"
CRS_METRIC = "EPSG:32636"          # UTM 36N, covers Kikuube

# A record counts as current if it is dated this year or later.
RECENT_FROM = 2020

# Record currency cut-offs over which the study area selection is repeated. The
# same district is selected at every one, so no single cut-off is defended.
CUTS = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70]

# One-way walking minutes. The JMP basic service standard is a 30 minute round
# trip including queuing; the friction surface yields one-way time, so the
# corresponding one-way threshold is 15 minutes. The sensitivity run uses the
# 30 minute one-way threshold applied by MacLachlan et al. (2024).
THRESHOLD_MIN = 15
THRESHOLD_SENSITIVITY = 30

# Repair budgets solved
K_LIST = [5, 10, 20]

# GHSL settlement classes. 11, 12, 13 are rural; 10 is water; 21 and above urban.
SMOD_RURAL = [11, 12, 13]
SMOD_WATER = 10

# WPdx usage_capacity, persons per point. 300 for handpumps and motorised pumps
# in Uganda, with 250 and 50 also occurring.
CAPACITY_DEFAULT = 300
