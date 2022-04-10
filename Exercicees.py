# 16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of
# rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP,
# which represents daily rainfall amounts. Make a visualization focusing on the
# data in this column. You can repeat the exercise for Death Valley if you’re
# curious how little rainfall occurs in a desert.
# 16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and
# Death Valley graphs reflect the different data ranges. To accurately compare
# the temperature range in Sitka to that of Death Valley, you need identical
# scales on the y-axis. Change the settings for the y-axis on one or both of the
# charts in Figures 16-5 and 16-6. Then make a direct comparison between
# temperature ranges in Sitka and Death Valley (or any two places you want to
# compare).
# 16-3. San Francisco: Are temperatures in San Francisco more like temperatures
# in Sitka or temperatures in Death Valley? Download some data for San
# Francisco, and generate a high-low temperature plot for San Francisco to
# make a comparison.Downloading Data 347
# 16-4. Automatic Indexes: In this section, we hardcoded the indexes corresponding
# to the TMIN and TMAX columns. Use the header row to determine the indexes
# for these values, so your program can work for Sitka or Death Valley. Use the
# station name to automatically generate an appropriate title for your graph
# as well.
# 16-5. Explore: Generate a few more visualizations that examine any other
# weather aspect you’re interested in for any locations you’re curious about.
# 16-6. Refactoring: The loop that pulls data from all_eq_dicts uses variables for
# the magnitude, longitude, latitude, and title of each earthquake
# before appending these values to their appropriate lists. This approach was
# chosen for clarity in how to pull data from a JSON file, but it’s not necessary in your code.
# Instead of using these temporary variables, pull each value from eq_dict and
# append it to the appropriate list in one line. Doing so should shorten the body
# of this loop to just four lines.
# 16-7. Automated Title: In this section, we specified the title manually when defining my_layout,
# which means we have to remember to update the title every
# time the source file changes. Instead, you can use the title for the data set in
# the metadata part of the JSON file. Pull this value, assign it to a variable, and
# use this for the title of the map when you’re defining my_layout.
# (continued)358 Chapter 16
# 16-8. Recent Earthquakes: You can find data files containing information about
# the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods
# online. Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
# and you’ll see a list of links to data sets for various time periods, focusing on
# earthquakes of different magnitudes. Download one of these data sets, and
# create a visualization of the most recent earthquake activity.
# 16-9. World Fires: In the resources for this chapter, you’ll find a file called
# world_fires_1_day.csv. This file contains information about fires burning in
# different locations around the globe, including the latitude and longitude, and the
# brightness of each fire. Using the data processing work from the first part of
# this chapter and the mapping work from this section, make a map that shows
# which parts of the world are affected by fires.
# You can download more recent versions of this data at https://earthdata
# .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You
# can find links to the data in CSV format in the TXT section.

