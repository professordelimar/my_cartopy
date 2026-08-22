"""RotatedPole projection example.

Author: Nelson Ribeiro-Filho
Repository: cartopy_projections
Output: images/rotated_pole.png
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

GOLD = "#FFD700"
OCEAN_BLUE = "#3B82C4"
COAST = "#202020"
GRID = "#6B7280"

projection = ccrs.RotatedPole(pole_longitude=177.5, pole_latitude=37.5)
fig = plt.figure(figsize=(10.5, 6.4))
ax = plt.axes(projection=projection)
ax.set_global()

land = cfeature.NaturalEarthFeature("physical", "land", "10m", edgecolor="none", facecolor=GOLD)
ocean = cfeature.NaturalEarthFeature("physical", "ocean", "10m", edgecolor="none", facecolor=OCEAN_BLUE)
lakes = cfeature.NaturalEarthFeature("physical", "lakes", "10m", edgecolor=COAST, facecolor=OCEAN_BLUE)
borders = cfeature.NaturalEarthFeature("cultural", "admin_0_boundary_lines_land", "10m", edgecolor="#333333", facecolor="none")

ax.add_feature(ocean, zorder=0)
ax.add_feature(land, zorder=1)
ax.add_feature(lakes, linewidth=0.25, zorder=2)
ax.add_feature(borders, linewidth=0.35, zorder=3)
ax.coastlines(resolution="10m", color=COAST, linewidth=0.45, zorder=4)
ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=0.35, color=GRID, alpha=0.45, linestyle="--")

fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.095)
fig.text(0.5, 0.035, 'Rotated Pole — latitude/longitude grid with a relocated geographic pole.', ha="center", va="center", fontsize=12, fontweight="semibold")

plt.savefig('images/rotated_pole.png', dpi=400, bbox_inches="tight", pad_inches=0.04, facecolor="white")
plt.show()
