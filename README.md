# BMKG-API-Scraper
A code to scrape [ibnux](https://github.com/ibnux)'s [BMKG Weather importer](https://www.bmkg.go.id) into a CSV file.

All data is owned and provided by [Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)](https://www.bmkg.go.id).

## Example output

| id                                | kota           | jamCuaca           | kodeCuaca | cuaca         | humidity | tempC | tempF |
|-----------------------------------|----------------|--------------------|-----------|---------------|----------|-------|-------|
| Banda_Aceh_2023-11-13T00:00:00     | Banda Aceh     | 2023-11-13 00:00:00 | 3         | Berawan       | 85       | 25    | 77    |
| Banda_Aceh_2023-11-13T06:00:00     | Banda Aceh     | 2023-11-13 06:00:00 | 95        | Hujan Petir   | 65       | 31    | 88    |
| Banda_Aceh_2023-11-13T12:00:00     | Banda Aceh     | 2023-11-13 12:00:00 | 1         | Cerah Berawan | 80       | 26    | 79    |
| Banda_Aceh_2023-11-13T18:00:00     | Banda Aceh     | 2023-11-13 18:00:00 | 60        | Hujan Ringan  | 90       | 23    | 73    |
| Bireuen_2023-11-13T00:00:00        | Bireuen        | 2023-11-13 00:00:00 | 1         | Cerah Berawan | 85       | 25    | 77    |
| Bireuen_2023-11-13T06:00:00        | Bireuen        | 2023-11-13 06:00:00 | 1         | Cerah Berawan | 65       | 31    | 88    |
| Bireuen_2023-11-13T12:00:00        | Bireuen        | 2023-11-13 12:00:00 | 60        | Hujan Ringan  | 80       | 26    | 79    |
| Bireuen_2023-11-13T18:00:00        | Bireuen        | 2023-11-13 18:00:00 | 60        | Hujan Ringan  | 90       | 23    | 73    |
| Gayo_Lues_2023-11-13T00:00:00      | Gayo Lues      | 2023-11-13 00:00:00 | 3         | Berawan       | 95       | 20    | 68    |
| Gayo_Lues_2023-11-13T06:00:00      | Gayo Lues      | 2023-11-13 06:00:00 | 60        | Hujan Ringan  | 75       | 26    | 79    |
| Gayo_Lues_2023-11-13T12:00:00      | Gayo Lues      | 2023-11-13 12:00:00 | 60        | Hujan Ringan  | 90       | 21    | 70    |
| Gayo_Lues_2023-11-13T18:00:00      | Gayo Lues      | 2023-11-13 18:00:00 | 1         | Cerah Berawan | 100      | 18    | 64    |
| Aceh_Barat_Daya_2023-11-13T00:00:00 | Aceh Barat Daya| 2023-11-13 00:00:00 | 3         | Berawan       | 85       | 25    | 77    |
| Aceh_Barat_Daya_2023-11-13T06:00:00 | Aceh Barat Daya| 2023-11-13 06:00:00 | 60        | Hujan Ringan  | 65       | 31    | 88    |
| Aceh_Barat_Daya_2023-11-13T12:00:00 | Aceh Barat Daya| 2023-11-13 12:00:00 | 60        | Hujan Ringan  | 80       | 26    | 79    |

