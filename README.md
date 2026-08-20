# Spatial optimisation of rural water point rehabilitation

Selecting non-functional water points for repair under a fixed budget in Kikuube District, Uganda.

MSc dissertation, CASA0010, Centre for Advanced Spatial Analysis, UCL. Ziyi Yuan, August 2026.

A district water office holds an inventory of broken water points and a budget expressed as a number
of repairs. This repository formulates that choice as a capacitated maximal covering location problem
and solves it to proven optimality, under two objectives and three budgets, with a sensitivity case
at a longer walking threshold.

## Data

| Dataset | Source | Version |
|---|---|---|
| Water points | [WPdx+](https://data.waterpointdata.org/dataset/Water-Point-Data-Exchange-Plus-WPdx-/eqje-vguj) | Uganda extract, 29 July 2026 |
| Administrative boundaries | [OCHA COD-AB](https://data.humdata.org/dataset/cod-ab-uga) | valid 2020-08-24 |
| Census | [UBOS](https://www.ubos.org/explore-statistics/20/) | NPHC 2024, subcounty profiles |
| Gridded population | [WorldPop](https://doi.org/10.5258/SOTON/WP00839) | R2025A v1, 100 m, constrained |
| Settlement classification | Earth Engine `JRC/GHSL/P2023A/GHS_SMOD_V2-0` | GHS-SMOD R2023A, 1 km |
| Friction surface | Earth Engine `Oxford/MAP/friction_surface_2019` | band `friction_walking_only` |

The two Earth Engine assets need an authenticated account. Input data is retrieved by the code rather
than committed here.

## Running it

```bash
pip install -r requirements.txt
earthengine authenticate
jupyter lab
```

Run the notebooks in numerical order. Each reads named inputs, performs one construction, and writes
named outputs that later notebooks read without recomputation. Analysis parameters, including the
walking threshold and the repair budgets, are held in `config.py`.

## Expected results

If the pipeline has run correctly:

- 98,774 records downloaded, 92,934 in the analysis sample
- 1,209 functioning points and 320 rehabilitation candidates in the study district
- 100,619 demand cells carrying 240,144 residents
- baseline coverage 171,138 of 240,144, or 71.3 per cent
- gains of 1,500, 3,000 and 5,889 people at budgets of 5, 10 and 20 repairs

## Licence

Code released under the MIT Licence. The datasets remain subject to the terms of their providers.

## Citation

> Yuan, Z. (2026) *Spatial optimisation of rural water point rehabilitation: selecting non-functional
> water points for repair under a fixed budget in Kikuube District, Uganda*. MSc dissertation,
> Centre for Advanced Spatial Analysis, University College London.
