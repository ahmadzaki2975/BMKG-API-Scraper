# BMKG-API-Scraper
A code to scrape [ibnux](https://github.com/ibnux)'s [BMKG Weather importer](https://www.bmkg.go.id) into a CSV file.

All data is owned and provided by [Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)](https://www.bmkg.go.id).

## Example output

| Kota               | Jam Cuaca           | Kode Cuaca      | Cuaca         | Humidity | Temp (C) | Temp (F) |
|--------------------|---------------------|-----------------|---------------|----------|----------|----------|
| Banda Aceh         | 2023-11-05 00:00:00 | 1               | Cerah Berawan | 85       | 24       | 75       |
| Banda Aceh         | 2023-11-05 06:00:00 | 3               | Berawan       | 65       | 31       | 88       |
| Banda Aceh         | 2023-11-05 12:00:00 | 3               | Berawan       | 80       | 26       | 79       |
| Banda Aceh         | 2023-11-05 18:00:00 | 1               | Cerah Berawan | 90       | 23       | 73       |
| Kab. Bireuen       | 2023-11-05 00:00:00 | 1               | Cerah Berawan | 85       | 24       | 75       |
| Kab. Bireuen       | 2023-11-05 06:00:00 | 60              | Hujan Ringan  | 65       | 31       | 88       |
| Kab. Bireuen       | 2023-11-05 12:00:00 | 1               | Cerah Berawan | 80       | 26       | 79       |
| Kab. Bireuen       | 2023-11-05 18:00:00 | 1               | Cerah Berawan | 90       | 23       | 73       |
| Kab. Gayo Lues     | 2023-11-05 00:00:00 | 1               | Cerah Berawan | 95       | 17       | 63       |
| Kab. Gayo Lues     | 2023-11-05 06:00:00 | 60              | Hujan Ringan  | 75       | 26       | 79       |
| Kab. Gayo Lues     | 2023-11-05 12:00:00 | 60              | Hujan Ringan  | 90       | 21       | 70       |
| Kab. Gayo Lues     | 2023-11-05 18:00:00 | 3               | Berawan       | 95       | 18       | 64       |
| Kab. Aceh Barat Daya| 2023-11-05 00:00:00 | 1              | Cerah Berawan | 85       | 24       | 75       |
| Kab. Aceh Barat Daya| 2023-11-05 06:00:00 | 60             | Hujan Ringan  | 65       | 31       | 88       |
| Kab. Aceh Barat Daya| 2023-11-05 12:00:00 | 95             | Hujan Petir   | 80       | 26       | 79       |
| Kab. Aceh Barat Daya| 2023-11-05 18:00:00 | 3              | Berawan       | 90       | 23       | 73       |
| Kab. Aceh Jaya     | 2023-11-05 00:00:00 | 3               | Berawan       | 85       | 24       | 75       |
| Kab. Aceh Jaya     | 2023-11-05 06:00:00 | 60              | Hujan Ringan  | 65       | 31       | 88       |
| Kab. Aceh Jaya     | 2023-11-05 12:00:00 | 1               | Cerah Berawan | 80       | 26       | 79       |
| Kab. Aceh Jaya     | 2023-11-05 18:00:00 | 3               | Berawan       | 90       | 23       | 73       |
| Kab. Aceh Timur    | 2023-11-05 00:00:00 | 3               | Berawan       | 85       | 24       | 75       |
| Kab. Aceh Timur    | 2023-11-05 06:00:00 | 1               | Cerah Berawan | 65       | 31       | 88       |
| Kab. Aceh Timur    | 2023-11-05 12:00:00 | 1               | Cerah Berawan | 80       | 26       | 79       |
| Kab. Aceh Timur    | 2023-11-05 18:00:00 | 1               | Cerah Berawan | 90       | 23       | 73       |
| Kab. Aceh Tamiang  | 2023-11-05 00:00:00 | 45              | Berkabut      | 85       | 24       | 75       |
| Kab. Aceh Tamiang  | 2023-11-05 06:00:00 | 1               | Cerah Berawan | 65       | 31       | 88       |
| Kab. Aceh Tamiang  | 2023-11-05 12:00:00 | 3               | Berawan       | 80       | 26       | 79       |
| Kab. Aceh Tamiang  | 2023-11-05 18:00:00 | 0               | Cerah         | 90       | 23       | 73       |
| Kab. Aceh Besar    | 2023-11-05 00:00:00 | 1               | Cerah Berawan | 85       | 24       | 75       |
| Kab. Aceh Besar    | 2023-11-05 06:00:00 | 60              | Hujan Ringan  | 65       | 31       | 88       |
| Kab. Aceh Besar    | 2023-11-05 12:00:00 | 45              | Berkabut      | 80       | 26       | 79       |
| Kab. Aceh Besar    | 2023-11-05 18:00:00 | 1               | Cerah Berawan | 90       | 23       | 73       |
| Kab. Aceh Tenggara | 2023-11-05 00:00:00 | 1               | Cerah Berawan | 95       | 17       | 63       |
| Kab. Aceh Tenggara |
