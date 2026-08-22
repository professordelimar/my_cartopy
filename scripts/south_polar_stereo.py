"""SouthPolarStereo projection example.

Author: Nelson Ribeiro-Filho
Repository: cartopy_projections
Output: images/south_polar_stereo.png
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

projection = ccrs.SouthPolarStereo(central_longitude=0)
fig = plt.figure(figsize=(10.5, 6.4))
ax = plt.axes(projection=projection)
ax.set_extent([-180, 180, -90, -45], crs=ccrs.PlateCarree())

# Cartopy's packaged shaded-relief raster provides a Basemap-like topographic style.
ax.stock_img()
ax.coastlines(resolution="10m", color="#202020", linewidth=0.45, zorder=3)
ax.add_feature(cfeature.BORDERS.with_scale("10m"), edgecolor="#333333", linewidth=0.35, zorder=3)
ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False, linewidth=0.35, color="#6B7280", alpha=0.45, linestyle="--")

fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.095)
fig.text(0.5, 0.035, 'South Polar Stereo — polar stereographic view of the Southern Hemisphere.', ha="center", va="center", fontsize=12, fontweight="semibold")

plt.savefig('images/south_polar_stereo.png', dpi=400, bbox_inches="tight", pad_inches=0.04, facecolor="white")
plt.show()
