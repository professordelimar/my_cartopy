# Projection catalog

## 1. PlateCarree

- Script: `scripts/plate_carree.py`
- Image: `images/plate_carree.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.PlateCarree()`
- Description: PlateCarree — equirectangular cylindrical projection.

## 2. AlbersEqualArea

- Script: `scripts/albers_equal_area.py`
- Image: `images/albers_equal_area.png`
- Style: gold land / blue ocean
- Extent: `[-85, -30, -60, 15]`
- Cartopy constructor: `ccrs.AlbersEqualArea(central_longitude=-55, central_latitude=-15, standard_parallels=(-5, -42))`
- Description: Albers Equal Area — conic equal-area projection.

## 3. AzimuthalEquidistant

- Script: `scripts/azimuthal_equidistant.py`
- Image: `images/azimuthal_equidistant.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.AzimuthalEquidistant(central_longitude=-50, central_latitude=-15)`
- Description: Azimuthal Equidistant — distances and directions are exact from the center.

## 4. EquidistantConic

- Script: `scripts/equidistant_conic.py`
- Image: `images/equidistant_conic.png`
- Style: gold land / blue ocean
- Extent: `[-85, -30, -60, 15]`
- Cartopy constructor: `ccrs.EquidistantConic(central_longitude=-55, central_latitude=-15, standard_parallels=(-5, -42))`
- Description: Equidistant Conic — true scale along selected standard parallels.

## 5. LambertConformal

- Script: `scripts/lambert_conformal.py`
- Image: `images/lambert_conformal.png`
- Style: topographic shaded relief
- Extent: `[-85, -30, -60, 15]`
- Cartopy constructor: `ccrs.LambertConformal(central_longitude=-55, central_latitude=-15, standard_parallels=(-5, -42))`
- Description: Lambert Conformal — conformal conic projection.

## 6. LambertCylindrical

- Script: `scripts/lambert_cylindrical.py`
- Image: `images/lambert_cylindrical.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.LambertCylindrical()`
- Description: Lambert Cylindrical — cylindrical equal-area projection.

## 7. Mercator

- Script: `scripts/mercator.py`
- Image: `images/mercator.png`
- Style: gold land / blue ocean
- Extent: `[-180, 180, -80, 80]`
- Cartopy constructor: `ccrs.Mercator()`
- Description: Mercator — conformal cylindrical projection.

## 8. Miller

- Script: `scripts/miller.py`
- Image: `images/miller.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.Miller()`
- Description: Miller — modified cylindrical projection for world maps.

## 9. Mollweide

- Script: `scripts/mollweide.py`
- Image: `images/mollweide.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.Mollweide()`
- Description: Mollweide — pseudocylindrical equal-area projection.

## 10. ObliqueMercator

- Script: `scripts/oblique_mercator.py`
- Image: `images/oblique_mercator.png`
- Style: gold land / blue ocean
- Extent: `[-120, 40, -70, 70]`
- Cartopy constructor: `ccrs.ObliqueMercator(central_longitude=-45, central_latitude=-10, azimuth=35)`
- Description: Oblique Mercator — Mercator projection along an oblique central line.

## 11. Orthographic

- Script: `scripts/orthographic.py`
- Image: `images/orthographic.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.Orthographic(central_longitude=-55, central_latitude=-15)`
- Description: Orthographic — globe-like perspective from an infinite viewing distance.

## 12. Robinson

- Script: `scripts/robinson.py`
- Image: `images/robinson.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.Robinson()`
- Description: Robinson — compromise projection designed for visually balanced world maps.

## 13. Sinusoidal

- Script: `scripts/sinusoidal.py`
- Image: `images/sinusoidal.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.Sinusoidal()`
- Description: Sinusoidal — pseudocylindrical equal-area projection.

## 14. Stereographic

- Script: `scripts/stereographic.py`
- Image: `images/stereographic.png`
- Style: gold land / blue ocean
- Extent: `[-120, 30, -70, 65]`
- Cartopy constructor: `ccrs.Stereographic(central_longitude=-50, central_latitude=-15)`
- Description: Stereographic — conformal azimuthal projection.

## 15. TransverseMercator

- Script: `scripts/transverse_mercator.py`
- Image: `images/transverse_mercator.png`
- Style: gold land / blue ocean
- Extent: `[-75, -27, -40, 15]`
- Cartopy constructor: `ccrs.TransverseMercator(central_longitude=-51, central_latitude=0)`
- Description: Transverse Mercator — conformal cylindrical projection rotated 90 degrees.

## 16. UTM

- Script: `scripts/utm_zone_22s.py`
- Image: `images/utm_zone_22s.png`
- Style: gold land / blue ocean
- Extent: `[-54, -48, -15, 5]`
- Cartopy constructor: `ccrs.UTM(zone=22, southern_hemisphere=True)`
- Description: UTM Zone 22S — Universal Transverse Mercator for a South American zone.

## 17. InterruptedGoodeHomolosine

- Script: `scripts/interrupted_goode_homolosine.py`
- Image: `images/interrupted_goode_homolosine.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.InterruptedGoodeHomolosine(emphasis="land")`
- Description: Interrupted Goode Homolosine — interrupted equal-area world projection.

## 18. RotatedPole

- Script: `scripts/rotated_pole.py`
- Image: `images/rotated_pole.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.RotatedPole(pole_longitude=177.5, pole_latitude=37.5)`
- Description: Rotated Pole — latitude/longitude grid with a relocated geographic pole.

## 19. OSGB

- Script: `scripts/osgb.py`
- Image: `images/osgb.png`
- Style: gold land / blue ocean
- Extent: `[-9, 3, 49, 61]`
- Cartopy constructor: `ccrs.OSGB()`
- Description: OSGB — British National Grid projection for Great Britain.

## 20. LambertZoneII

- Script: `scripts/lambert_zone_ii.py`
- Image: `images/lambert_zone_ii.png`
- Style: gold land / blue ocean
- Extent: `[-6, 10, 41, 52]`
- Cartopy constructor: `ccrs.LambertZoneII()`
- Description: Lambert Zone II — legacy Lambert projection for metropolitan France.

## 21. EuroPP

- Script: `scripts/europp.py`
- Image: `images/europp.png`
- Style: gold land / blue ocean
- Extent: `[5, 15, 44, 60]`
- Cartopy constructor: `ccrs.EuroPP()`
- Description: EuroPP — ED50 / UTM Zone 32N projection used for a European domain.

## 22. Geostationary

- Script: `scripts/geostationary.py`
- Image: `images/geostationary.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.Geostationary(central_longitude=-60)`
- Description: Geostationary — satellite view from geostationary orbit.

## 23. NearsidePerspective

- Script: `scripts/nearside_perspective.py`
- Image: `images/nearside_perspective.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.NearsidePerspective(central_longitude=-55, central_latitude=-15)`
- Description: Nearside Perspective — finite-distance perspective view of the globe.

## 24. EckertI

- Script: `scripts/eckert_i.py`
- Image: `images/eckert_i.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.EckertI()`
- Description: Eckert I — pseudocylindrical projection with straight meridians and parallels.

## 25. EckertII

- Script: `scripts/eckert_ii.py`
- Image: `images/eckert_ii.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.EckertII()`
- Description: Eckert II — pseudocylindrical equal-area projection.

## 26. EckertIII

- Script: `scripts/eckert_iii.py`
- Image: `images/eckert_iii.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.EckertIII()`
- Description: Eckert III — pseudocylindrical projection with elliptical meridians.

## 27. EckertIV

- Script: `scripts/eckert_iv.py`
- Image: `images/eckert_iv.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.EckertIV()`
- Description: Eckert IV — pseudocylindrical equal-area world projection.

## 28. EckertV

- Script: `scripts/eckert_v.py`
- Image: `images/eckert_v.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.EckertV()`
- Description: Eckert V — pseudocylindrical projection with sinusoidal meridians.

## 29. EckertVI

- Script: `scripts/eckert_vi.py`
- Image: `images/eckert_vi.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.EckertVI()`
- Description: Eckert VI — pseudocylindrical equal-area projection.

## 30. Spilhaus

- Script: `scripts/spilhaus.py`
- Image: `images/spilhaus.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.Spilhaus(rotation=45)`
- Description: Spilhaus — square world-ocean map emphasizing continuity of the oceans.

## 31. Aitoff

- Script: `scripts/aitoff.py`
- Image: `images/aitoff.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.Aitoff()`
- Description: Aitoff — modified azimuthal projection balancing shape and scale.

## 32. EqualEarth

- Script: `scripts/equal_earth.py`
- Image: `images/equal_earth.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.EqualEarth()`
- Description: Equal Earth — pseudocylindrical equal-area projection for world maps.

## 33. Gnomonic

- Script: `scripts/gnomonic.py`
- Image: `images/gnomonic.png`
- Style: gold land / blue ocean
- Extent: `[-90, 10, -30, 70]`
- Cartopy constructor: `ccrs.Gnomonic(central_longitude=-40, central_latitude=20)`
- Description: Gnomonic — great-circle routes appear as straight lines.

## 34. Hammer

- Script: `scripts/hammer.py`
- Image: `images/hammer.png`
- Style: topographic shaded relief
- Extent: `global`
- Cartopy constructor: `ccrs.Hammer()`
- Description: Hammer — modified azimuthal equal-area world projection.

## 35. LambertAzimuthalEqualArea

- Script: `scripts/lambert_azimuthal_equal_area.py`
- Image: `images/lambert_azimuthal_equal_area.png`
- Style: gold land / blue ocean
- Extent: `global`
- Cartopy constructor: `ccrs.LambertAzimuthalEqualArea(central_longitude=-55, central_latitude=-15)`
- Description: Lambert Azimuthal Equal Area — azimuthal equal-area projection.

## 36. NorthPolarStereo

- Script: `scripts/north_polar_stereo.py`
- Image: `images/north_polar_stereo.png`
- Style: topographic shaded relief
- Extent: `[-180, 180, 45, 90]`
- Cartopy constructor: `ccrs.NorthPolarStereo(central_longitude=0)`
- Description: North Polar Stereo — polar stereographic view of the Northern Hemisphere.

## 37. OSNI

- Script: `scripts/osni.py`
- Image: `images/osni.png`
- Style: gold land / blue ocean
- Extent: `[-11, -5, 51, 56]`
- Cartopy constructor: `ccrs.OSNI()`
- Description: OSNI — Ordnance Survey projection for Northern Ireland.

## 38. SouthPolarStereo

- Script: `scripts/south_polar_stereo.py`
- Image: `images/south_polar_stereo.png`
- Style: topographic shaded relief
- Extent: `[-180, 180, -90, -45]`
- Cartopy constructor: `ccrs.SouthPolarStereo(central_longitude=0)`
- Description: South Polar Stereo — polar stereographic view of the Southern Hemisphere.
