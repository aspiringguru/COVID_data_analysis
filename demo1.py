import pandas as pd
import os

mypath = "../data.bls.gov/unemployment_rate/"

file_list = []
for file in os.listdir(mypath):
    if file.endswith(".xlsx"):
        print(os.path.join(mypath, file))
        file_list.append(os.path.join(mypath, file))

file_list

col_names =  []
combined_results  = pd.DataFrame(columns = col_names)


for filename in file_list:
    # Read File
    print("opening filename:", filename)
    df = pd.read_excel(filename, sheet_name="BLS Data Series")
    #df = pd.read_excel(file_list[0], sheet_name="BLS Data Series")
    #df.shape
    series_id = df.iloc[2,1]
    print("series_id:", series_id)
    series_id_text = df.iloc[4,1]
    print("series_id_text:", series_id_text)
    #now detect rownumber where data starts and ends.
    #find row with first value of 'Year' in column 0
    #and first non null value in column 0 after that.
    first_col = df.iloc[:, 0]
    #first_col
    start_row_index = first_col[first_col == 'Year'].index[0]
    #start_row_index
    last_row_index = len(first_col)
    #last_row_index

    df_data = df.iloc[start_row_index+1:last_row_index,0:13]
    #df_data

    #df_info = df.iloc[4:9,0:2]
    #df_data = df.iloc[11:32,0:13]
    new_col_names = list(df.iloc[start_row_index, :])
    #new_col_names

    print("df_data.shape:", df_data.shape)
    #print(df_data.head())
    df_data.columns = new_col_names
    #print(df_data.head())

    #df_data

    df_data_cleaned = pd.melt(df_data, id_vars=['Year'])
    df_data_cleaned = df_data.melt('Year')

    df_data_cleaned['date'] = df_data_cleaned['Year'].astype('str') + '-' + df_data_cleaned['variable']
    #df_data_cleaned
    df_data_cleaned.drop(['Year', 'variable'], axis=1, inplace=True)
    #df_data_cleaned
    df_data_cleaned.dropna(inplace=True)
    df_data_cleaned.rename(columns={"value": series_id}, inplace=True)
    #
    print("df_data_cleaned\n", df_data_cleaned)
    #series_id
    #series_id_text
    output_filename = filename+"_"+series_id+"_"+series_id_text+".csv"
    print("saving as csv file:", output_filename)
    df_data_cleaned[['date', series_id]].to_csv(output_filename, index=False)
    #df_data_cleaned
    #append x to combined_results
    if len(combined_results.columns)==0:
        print("combined_results is empty. combined_results.shape=", combined_results.shape)
        combined_results = df_data_cleaned[['date', series_id]]
    else:
        print("combined_results not empty, joining column from df_data_cleaned")
        #add the series_id column to combined_results (years should be the same)
        combined_results[series_id] = df_data_cleaned[series_id]
    print("after adding new data column, combined_results.shape:", combined_results.shape)
combined_results.to_csv(mypath+"combined_results.csv", index=False)
