# Cartopy Projections Gallery

<<<<<<< HEAD
A reproducible gallery of **all 38 projections listed in the Cartopy 0.25 projection reference**, with one standalone Python script and one rendered PNG for each projection. The collection mixes a high-contrast cartographic style (gold land and blue ocean) with selected shaded-relief maps.

**Author:** Nelson Ribeiro-Filho  
**Copyright:** © 2026 64.200.407 NELSON DE LIMA RIBEIRO FILHO - ME. All rights reserved.

## Design

- Vector maps use Natural Earth **10m** coastlines, land, ocean, lakes and national boundaries.
- Land color: `#FFD700` (gold).
- Ocean color: `#3B82C4` (blue).
- Selected projections use `ax.stock_img()` for a Basemap-like shaded-relief appearance.
- Final scripts save at **400 dpi**.
- Figures contain **no title**; only a concise projection description is printed below the map.
- Appropriate geographic extents are used for regional systems such as UTM, OSGB, Lambert Zone II, EuroPP and OSNI.

## Installation

The most robust installation is through conda-forge:

```bash
conda create -n cartopy-projections -c conda-forge python=3.12 cartopy=0.25 matplotlib proj>=9.6
conda activate cartopy-projections
```

A standard pip environment can run every projection supported by its bundled PROJ version:

```bash
pip install -r requirements.txt
```

> **Spilhaus:** Cartopy 0.25 added this projection and it requires **PROJ 9.6+**. If a pip environment ships an older PROJ library, use the conda-forge environment above.

On the first vector-map run, Cartopy may download the Natural Earth 10m datasets into its local cache.

## Run

Run a single projection from the repository root:

```bash
python scripts/robinson.py
```

Or regenerate the complete gallery:

```bash
python run_all.py
```

## Projection gallery

| # | Cartopy class | Style | Script | Preview |
|---:|---|---|---|---|
| 1 | `PlateCarree` | Gold/blue vector | [`scripts/plate_carree.py`](scripts/plate_carree.py) | ![PlateCarree](images/plate_carree.png) |
| 2 | `AlbersEqualArea` | Gold/blue vector | [`scripts/albers_equal_area.py`](scripts/albers_equal_area.py) | ![AlbersEqualArea](images/albers_equal_area.png) |
| 3 | `AzimuthalEquidistant` | Gold/blue vector | [`scripts/azimuthal_equidistant.py`](scripts/azimuthal_equidistant.py) | ![AzimuthalEquidistant](images/azimuthal_equidistant.png) |
| 4 | `EquidistantConic` | Gold/blue vector | [`scripts/equidistant_conic.py`](scripts/equidistant_conic.py) | ![EquidistantConic](images/equidistant_conic.png) |
| 5 | `LambertConformal` | Topographic | [`scripts/lambert_conformal.py`](scripts/lambert_conformal.py) | ![LambertConformal](images/lambert_conformal.png) |
| 6 | `LambertCylindrical` | Gold/blue vector | [`scripts/lambert_cylindrical.py`](scripts/lambert_cylindrical.py) | ![LambertCylindrical](images/lambert_cylindrical.png) |
| 7 | `Mercator` | Gold/blue vector | [`scripts/mercator.py`](scripts/mercator.py) | ![Mercator](images/mercator.png) |
| 8 | `Miller` | Gold/blue vector | [`scripts/miller.py`](scripts/miller.py) | ![Miller](images/miller.png) |
| 9 | `Mollweide` | Topographic | [`scripts/mollweide.py`](scripts/mollweide.py) | ![Mollweide](images/mollweide.png) |
| 10 | `ObliqueMercator` | Gold/blue vector | [`scripts/oblique_mercator.py`](scripts/oblique_mercator.py) | ![ObliqueMercator](images/oblique_mercator.png) |
| 11 | `Orthographic` | Topographic | [`scripts/orthographic.py`](scripts/orthographic.py) | ![Orthographic](images/orthographic.png) |
| 12 | `Robinson` | Topographic | [`scripts/robinson.py`](scripts/robinson.py) | ![Robinson](images/robinson.png) |
| 13 | `Sinusoidal` | Gold/blue vector | [`scripts/sinusoidal.py`](scripts/sinusoidal.py) | ![Sinusoidal](images/sinusoidal.png) |
| 14 | `Stereographic` | Gold/blue vector | [`scripts/stereographic.py`](scripts/stereographic.py) | ![Stereographic](images/stereographic.png) |
| 15 | `TransverseMercator` | Gold/blue vector | [`scripts/transverse_mercator.py`](scripts/transverse_mercator.py) | ![TransverseMercator](images/transverse_mercator.png) |
| 16 | `UTM` | Gold/blue vector | [`scripts/utm_zone_22s.py`](scripts/utm_zone_22s.py) | ![UTM](images/utm_zone_22s.png) |
| 17 | `InterruptedGoodeHomolosine` | Gold/blue vector | [`scripts/interrupted_goode_homolosine.py`](scripts/interrupted_goode_homolosine.py) | ![InterruptedGoodeHomolosine](images/interrupted_goode_homolosine.png) |
| 18 | `RotatedPole` | Gold/blue vector | [`scripts/rotated_pole.py`](scripts/rotated_pole.py) | ![RotatedPole](images/rotated_pole.png) |
| 19 | `OSGB` | Gold/blue vector | [`scripts/osgb.py`](scripts/osgb.py) | ![OSGB](images/osgb.png) |
| 20 | `LambertZoneII` | Gold/blue vector | [`scripts/lambert_zone_ii.py`](scripts/lambert_zone_ii.py) | ![LambertZoneII](images/lambert_zone_ii.png) |
| 21 | `EuroPP` | Gold/blue vector | [`scripts/europp.py`](scripts/europp.py) | ![EuroPP](images/europp.png) |
| 22 | `Geostationary` | Topographic | [`scripts/geostationary.py`](scripts/geostationary.py) | ![Geostationary](images/geostationary.png) |
| 23 | `NearsidePerspective` | Topographic | [`scripts/nearside_perspective.py`](scripts/nearside_perspective.py) | ![NearsidePerspective](images/nearside_perspective.png) |
| 24 | `EckertI` | Gold/blue vector | [`scripts/eckert_i.py`](scripts/eckert_i.py) | ![EckertI](images/eckert_i.png) |
| 25 | `EckertII` | Gold/blue vector | [`scripts/eckert_ii.py`](scripts/eckert_ii.py) | ![EckertII](images/eckert_ii.png) |
| 26 | `EckertIII` | Gold/blue vector | [`scripts/eckert_iii.py`](scripts/eckert_iii.py) | ![EckertIII](images/eckert_iii.png) |
| 27 | `EckertIV` | Topographic | [`scripts/eckert_iv.py`](scripts/eckert_iv.py) | ![EckertIV](images/eckert_iv.png) |
| 28 | `EckertV` | Gold/blue vector | [`scripts/eckert_v.py`](scripts/eckert_v.py) | ![EckertV](images/eckert_v.png) |
| 29 | `EckertVI` | Gold/blue vector | [`scripts/eckert_vi.py`](scripts/eckert_vi.py) | ![EckertVI](images/eckert_vi.png) |
| 30 | `Spilhaus` | Gold/blue vector | [`scripts/spilhaus.py`](scripts/spilhaus.py) | ![Spilhaus](images/spilhaus.png) |
| 31 | `Aitoff` | Gold/blue vector | [`scripts/aitoff.py`](scripts/aitoff.py) | ![Aitoff](images/aitoff.png) |
| 32 | `EqualEarth` | Topographic | [`scripts/equal_earth.py`](scripts/equal_earth.py) | ![EqualEarth](images/equal_earth.png) |
| 33 | `Gnomonic` | Gold/blue vector | [`scripts/gnomonic.py`](scripts/gnomonic.py) | ![Gnomonic](images/gnomonic.png) |
| 34 | `Hammer` | Topographic | [`scripts/hammer.py`](scripts/hammer.py) | ![Hammer](images/hammer.png) |
| 35 | `LambertAzimuthalEqualArea` | Gold/blue vector | [`scripts/lambert_azimuthal_equal_area.py`](scripts/lambert_azimuthal_equal_area.py) | ![LambertAzimuthalEqualArea](images/lambert_azimuthal_equal_area.png) |
| 36 | `NorthPolarStereo` | Topographic | [`scripts/north_polar_stereo.py`](scripts/north_polar_stereo.py) | ![NorthPolarStereo](images/north_polar_stereo.png) |
| 37 | `OSNI` | Gold/blue vector | [`scripts/osni.py`](scripts/osni.py) | ![OSNI](images/osni.png) |
| 38 | `SouthPolarStereo` | Topographic | [`scripts/south_polar_stereo.py`](scripts/south_polar_stereo.py) | ![SouthPolarStereo](images/south_polar_stereo.png) |

## Notes on resolution and data

Natural Earth 10m is used for the highest standard Natural Earth vector detail directly exposed by Cartopy's feature workflow. Shaded-relief examples intentionally use Cartopy's packaged stock raster to remain reproducible without third-party web tiles.

## Validation and reproducibility

All 38 projection scripts and `run_all.py` have been syntax-validated, and all 38 PNG previews are included at 400 dpi. The build environment used equivalent PROJ/Basemap rendering for the committed previews because Cartopy was unavailable there; the files in `scripts/` are Cartopy-native. Use `environment.yml` and `python run_all.py` to regenerate the complete gallery directly with Cartopy. See [`VALIDATION.txt`](VALIDATION.txt) for details.

## Sources and attribution

Cartopy is a third-party project released under the BSD 3-Clause license. Matplotlib, PROJ, pyproj, Shapely and Natural Earth retain their respective licenses and attribution requirements. No third-party code is relicensed by this repository.

## License

The original scripts, repository organization and generated gallery created for this project are proprietary. See [`LICENSE`](LICENSE). Third-party dependencies remain under their own licenses.
=======
A repository dedicated to illustrating examples of Cartopy usage for creating maps and geospatial visualizations in Python.

The project explores different map projections, coordinate reference systems, map customization, and the visualization of geographic and scientific data using the Python scientific ecosystem.

Objectives
* Demonstrate the use of Cartopy for map creation;
* Explore different cartographic projections;
* Illustrate geospatial data visualization techniques;
* Provide practical examples for learning and reference;
* Support the development of cartographic and scientific visualizations in Python.

Technologies
* **Python**;
* Cartopy;
* Matplotlib;
* NumPy;
* Pandas

Contents

The repository contains practical examples covering different aspects of Cartopy, including map projections, coordinate systems, geographic features, map customization, and spatial data visualization.

This repository is intended as a practical and educational reference for students, researchers, and developers working with cartography, geospatial analysis, geosciences, and scientific visualization.
>>>>>>> 2968fd297fa0ec062f371c816c4ceb39f14800b4
