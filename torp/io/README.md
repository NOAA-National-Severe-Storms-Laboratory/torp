
## Description of TORP Dataset  

| **Field**           | **Description**                                       | **Format / Example** |
|:---------------------|:---------------------------------------------------|:----------------|
| **timestamp**      | Valid time of the data entry                      | `YYYYMMDD-hhmm` (e.g., `20240305-1530`) |
| **year**           | Calendar year                                      | `YYYY` (e.g., `2024`) |
| **month**          | Calendar month                                     | `MM` (e.g., `03`) |
| **time**           | Time in hours/minutes (leading zeros dropped)      | `HHmm` or `mm` (e.g., `530`, `45`) |
| **unixTime**       | Seconds since **January 1, 1970** (Unix epoch)     | Integer (e.g., `1709637000`) |
| **latitude**       | Geographic latitude in degrees                    | Decimal (e.g., `35.6789`) |
| **longitude**      | Geographic longitude in degrees (negative for W)  | Decimal (e.g., `-97.1234`) |
| **radar**          | 4-letter radar station identifier                  | String (e.g., `KTLX`) |
| **rangeKm**        | Distance to the nearest radar (km)                 | Float (e.g., `34.5`) |
| **beginTimestamp** | _(Missing description - add details here)_         | _(Format?)_ |
