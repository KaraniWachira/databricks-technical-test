# Write a query that will display the results below (Note: some columns might be renamed
# but use the column names above). It should only show 2020 data and order by driver
# points.


# Filter the data to only show rows where the year is 2020. I took the dataframe name as race_results
race_results_2020 = race_results[race_results['year'] == 2020]

# Sort the results by driver points in descending order from the dataframe loaded
race_results_2020 = race_results_2020.sort_values(by='points', ascending=False)

# Display the results
print(race_results_2020)
