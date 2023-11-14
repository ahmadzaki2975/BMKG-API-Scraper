# BMKG-API-Scraper
A code to scrape [ibnux](https://github.com/ibnux)'s [BMKG Weather importer](https://www.bmkg.go.id) into a CSV file.

All data is owned and provided by [Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)](https://www.bmkg.go.id).

## Example output

| id                                 | kota         | jamCuaca            | kodeCuaca | cuaca         | humidity | tempC | tempF |
|------------------------------------|--------------|---------------------|-----------|---------------|----------|-------|-------|
| Banda Aceh_2023-11-14T00:00:00      | Banda Aceh   | 2023-11-14 00:00:00 | 60        | Hujan Ringan  | 85       | 25    | 77    |
| Banda Aceh_2023-11-14T06:00:00      | Banda Aceh   | 2023-11-14 06:00:00 | 1         | Cerah Berawan | 65       | 31    | 88    |
| Banda Aceh_2023-11-14T12:00:00      | Banda Aceh   | 2023-11-14 12:00:00 | 3         | Berawan       | 85       | 26    | 79    |
| Banda Aceh_2023-11-14T18:00:00      | Banda Aceh   | 2023-11-14 18:00:00 | 1         | Cerah Berawan | 90       | 23    | 73    |
| Bireuen_2023-11-14T00:00:00         | Bireuen      | 2023-11-14 00:00:00 | 1         | Cerah Berawan | 85       | 25    | 77    |
| Bireuen_2023-11-14T06:00:00         | Bireuen      | 2023-11-14 06:00:00 | 1         | Cerah Berawan | 65       | 31    | 88    |
| Bireuen_2023-11-14T12:00:00         | Bireuen      | 2023-11-14 12:00:00 | 3         | Berawan       | 85       | 26    | 79    |
| Bireuen_2023-11-14T18:00:00         | Bireuen      | 2023-11-14 18:00:00 | 1         | Cerah Berawan | 90       | 23    | 73    |
| Gayo Lues_2023-11-14T00:00:00       | Gayo Lues    | 2023-11-14 00:00:00 | 1         | Cerah Berawan | 95       | 20    | 68    |
| Gayo Lues_2023-11-14T06:00:00       | Gayo Lues    | 2023-11-14 06:00:00 | 60        | Hujan Ringan  | 75       | 26    | 79    |
| Gayo Lues_2023-11-14T12:00:00       | Gayo Lues    | 2023-11-14 12:00:00 | 60        | Hujan Ringan  | 95       | 21    | 70    |
| Gayo Lues_2023-11-14T18:00:00       | Gayo Lues    | 2023-11-14 18:00:00 | 1         | Cerah Berawan | 100      | 18    | 64    |
| Aceh Barat Daya_2023-11-14T00:00:00 | Aceh Barat Daya | 2023-11-14 00:00:00 | 60        | Hujan Ringan  | 85       | 25    | 77    |
| Aceh Barat Daya_2023-11-14T06:00:00 | Aceh Barat Daya | 2023-11-14 06:00:00 | 60        | Hujan Ringan  | 65       | 31    | 88    |
| Aceh Barat Daya_2023-11-14T12:00:00 | Aceh Barat Daya | 2023-11-14 12:00:00 | 60        | Hujan Ringan  | 85       | 26    | 79    |
| Aceh Barat Daya_2023-11-14T18:00:00 | Aceh Barat Daya | 2023-11-14 18:00:00 | 3         | Berawan       | 90       | 23    | 73    |
| Aceh Jaya_2023-11-14T00:00:00       | Aceh Jaya    | 2023-11-14 00:00:00 | 1         | Cerah Berawan | 85       | 25    | 77    |
| Aceh Jaya_2023-11-14T06:00:00       | Aceh Jaya    | 2023-11-14 06:00:00 | 60        | Hujan Ringan  | 65       | 31    | 88    |
| Aceh Jaya_2023-11-14T12:00:00       | Aceh Jaya    | 2023-11-14 12:00:00 | 60        | Hujan Ringan  | 85       | 26    | 79    |
| Aceh Jaya_2023-11-14T18:00:00       | Aceh Jaya    | 2023-11-14 18:00:00 | 3         | Berawan       | 90       | 23    | 73    |
| Aceh Timur_2023-11-14T00:00:00      | Aceh Timur   | 2023-11-14 00:00:00 | 1         | Cerah Berawan | 85       | 25    | 77    |
| ...                                | ...          | ...                 | ...       | ...           | ...      | ...   | ...   |


