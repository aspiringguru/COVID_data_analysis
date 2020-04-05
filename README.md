

#environment setup

dev machine

18.04.3 LTS (Bionic Beaver)
Ubuntu 18.04.3 LTS"
via ubuntu app Windows10 .


cd /mnt/d/2020/coding/covidData/coding
python3 -m venv env
source env/bin/activate

pip install --upgrade pip

pip install matplotlib
pip install pillow
pip install pandas
pip install xlrd openpyxl


reshape the data frame from
df_data.head()
Year   Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov  Dec
2000  12.7  13.8  13.3  12.6  12.8  12.3  13.4    14    13  12.8    13 13.2
2001  13.8  13.7  13.8  13.9  13.4  14.2  14.4  15.6  15.2    16  15.9    17
2002  16.5    16  16.6  16.7  16.6  16.7  16.8    17  16.3  15.1  17.1  16.9

to

Year Month Value
2000 Jan   12.7
2000 Feb   13.8
2000 Mar   13.3


etc





df_data[['Year', 'Jan']].melt(id_vars=['Year', 'Jan'])

https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-by-melt
