
## Description of TORP Dataset  

| **Field**        | **Description**                                           | **Unit**    | **Format / Example**                    |
|:-----------------|:----------------------------------------------------------|:------------|:----------------------------------------|
| timestamp        | Valid time of the data entry                              | \-          | `YYYYMMDD-hhmm` (e.g., `20240305-1530`) |
| year             | Calendar year                                             | \-          | `YYYY` (e.g., `2024`)                   |
| month            | Calendar month                                            | \-          | `MM` (e.g., `03`)                       |
| day              | Calendar day                                              | \-          | `DD` (e.g., `05`)                       |
| time             | Time in hours/minutes                                     | \-          | `HHmm` (e.g., `0530`)                   |
| unixTime         | Seconds since **January 1, 1970** (Unix epoch)            | s           | Integer (e.g., `1709637000`)            |
| latitude         | Geographic latitude                                       | °           | Decimal (e.g., `35.6789`)               |
| longitude        | Geographic longitude (negative for W)                     | °           | Decimal (e.g., `-97.1234`)              |
| radar            | 4-letter radar station identifier (ICAO)                  | \-          | String (e.g., `KTLX`)                   |
| rangeKm          | Distance to the nearest (dual-pol) radar                  | km          | Float (e.g., `34.5`)                    |
| beginTimestamp   | Report start time                                         | \-          | `YYYYMMDD-hhmm` (e.g., `20240305-1530`) |
| beginYear        | Report start year                                         | \-          | `YYYY` (e.g., `2024`)                   |
| beginMonth       | Report start month                                        | \-          | MM (e.g., `03`)                         |
| beginDay         | Report start day                                          | \-          | DD (e.g., `05`)                         |
| beginTime        | Report start time in                                      | \-          | HHmm (e.g., `0530`)                     |
| beginUnix        | Report start time in seconds since January 1, 1970 (Unix epoch) | s           | Integer (e.g., `1709637000`)      |
| beginLongitude   | Report start geographic latitude                          | °           | Decimal (e.g., `35.6789`)               |
| beginLatitude    | Report start geographic longitude (negative for W)        | °           | Decimal (e.g., `-97.1234`)              |
| endTimestamp     | Report end time                                           | \-          | YYYYMMDD-hhmm (e.g., `20240305-1530`)   |
| endYear          | Report end year                                           | \-          | YYYY (e.g., `2024`)                     |
| endMonth         | Report end month                                          | \-          | MM (e.g., `03`)                         |
| endDay           | Report end day                                            | \-          | DD (e.g., `05`)                         |
| endTime          | Report end time in                                        | \-          | HHmm (e.g., `0530`)                     |
| endUnix          | Report end time in seconds since January 1, 1970 (Unix epoch) | s           | Integer (e.g., `1709637000`)        |
| endLongitude     | Report end geographic latitude                            | °           | Decimal (e.g., `35.6789`)               |
| endLatitude      | Report end geographic longitude (negative for W)          | °           | Decimal (e.g., `-97.1234`)              |
| durationMin      | Duration of hazard                                        | min         | Integer (e.g., `90`)                    |
| tornado          | Binary flag for whether the report is a tornado report    | \-          | Boolean/Integer (`1` or `0`)            |
| spout            | Binary flag for landspout/waterspouts (from report text/manual classification) | \-          | Boolean/Integer (`1` or `0`) |
| anticyclonic     | Binary flag for anticyclonic tornadoes (from report text) | \-          | Boolean/Integer (`1` or `0`)           |
| hail             | Binary flag for whether the report is a hail report       | \-          | Boolean/Integer (`1` or `0`)           |
| wind             | Binary flag for whether the report is a wind report       | \-          | Boolean/Integer (`1` or `0`)           |
| severeType       | `Wind`, `Hail`, `Tornado`, or `-99900`. `-99900` is used for sub-severe (<50 kts or 1 in) reports. | \-          | String |
| magnitude        | EF-rating for tornadoes, hail size in inches, or wind speed in knots   | EF/F/in/kts | String/float/integer      |
| magnitudeType    | For wind magnitudes. EG = Wind Estimated Gust; ES = Estimated Sustained Wind; MS = Measured Sustained Wind;<br>MG = Measured Wind Gust. | \-            | String             |
| type                              |                                                           |             |                                |
| tornadoLength                     | From Storm Data: Length of the tornado or tornado segment while on the ground.  | mi          | Float    |
| tornadoWidth                      | From Storm Data: Width of the tornado or tornado segment while on the ground.   | yd          | Integer  |
| injuriesDirect                    |                                                           |             |                                |
| injuriesIndirect                  |                                                           |             |                                |
| deathsDirect                      |                                                           |             |                                |
| deathsIndirect                    |                                                           |             |                                |
| damageProperty                    |                                                           |             |                                |
| damageCrops                       |                                                           |             |                                |
| source                            |                                                           |             |                                |
| overview                          |                                                           |             |                                |
| details                           |                                                           |             |                                |
| stormEventsEpisodeID              |                                                           |             |                                |
| stormEventsReportID               |                                                           |             |                                |
| oneTorID                          |                                                           |             |                                |
| multiSegment                      |                                                           |             |                                |
| previousSegment                   |                                                           |             |                                |
| totalDurationMin                  |                                                           |             |                                |
| maxMagnitudeAcrossSeg             |                                                           |             |                                |
| totalTornadoLength                |                                                           |             |                                |
| maxTornadoWidth                   |                                                           |             |                                |
| totalInjuriesDirect               |                                                           |             |                                |
| totalInjuriesIndirect             |                                                           |             |                                |
| totalDeathsDirect                 |                                                           |             |                                |
| totalDeathsIndirect               |                                                           |             |                                |
| totalDamageProperty               |                                                           |             |                                |
| totalDamageCrops                  |                                                           |             |                                |
| preTornadoTracked                 |                                                           |             |                                |
| stormID                           |                                                           |             |                                |
| stormType                         |                                                           |             |                                |
| county                            |                                                           |             |                                |
| state                             |                                                           |             |                                |
| CWA                               |                                                           |             |                                |
| NWSRegion                         |                                                           |             |                                |
| QCd                               |                                                           |             |                                |
| corrected                         |                                                           |             |                                |
| QCnotes                           |                                                           |             |                                |
| autoQCnotes                       |                                                           |             |                                |
| season                            |                                                           |             |                                |
| minutesFromReport                 |                                                           |             |                                |
| minutesFromTornado                | Within 300 km                                             |             |                                |
| distanceToNearestTornadoWithin1Hr | Within 300 km                                             |             |                                |
| populationDensity_15_min                     |                                                |             |                                |
| populationDensity_2pt5_min                   |                                                |             |                                |
| populationDensity_30_sec                     |                                                |             |                                |
| warned                                       |                                                |             |                                |
| warningID                                    |                                                |             |                                |
| warningType                                  |                                                |             |                                |
| warningArea                                  |                                                |             |                                |
| warningTornadoTag                            |                                                |             |                                |
| warningDamageTag                             |                                                |             |                                |
| pointWarningLeadTime                         |                                                |             |                                |
| overallWarningLeadTime                       |                                                |             |                                |
| rangeAzShearMax                              |                                                |             |                                |
| rng_int                                      |                                                |             |                                |
| radarTimestamp                               |                                                |             |                                |
| latitudeAzShearMax                           |                                                |             |                                |
| longitudeAzShearMax                          |                                                |             |                                |
| distToAzShearMax                             |                                                |             |                                |
| AzShear_max                                  |                                                |             |                                |
| AzShear_mean                                 |                                                |             |                                |
| AzShear_min                                  |                                                |             |                                |
| AzShear_25th_percentile                      |                                                |             |                                |
| AzShear_median                               |                                                |             |                                |
| AzShear_75th_percentile                      |                                                |             |                                |
| DivShear_max                                 |                                                |             |                                |
| DivShear_mean                                |                                                |             |                                |
| DivShear_min                                 |                                                |             |                                |
| DivShear_25th_percentile                     |                                                |             |                                |
| DivShear_median                              |                                                |             |                                |
| DivShear_75th_percentile                     |                                                |             |                                |
| PhiDP_AzGradient_max                         |                                                |             |                                |
| PhiDP_AzGradient_mean                        |                                                |             |                                |
| PhiDP_AzGradient_min                         |                                                |             |                                |
| PhiDP_AzGradient_25th_percentile             |                                                |             |                                |
| PhiDP_AzGradient_median                      |                                                |             |                                |
| PhiDP_AzGradient_75th_percentile             |                                                |             |                                |
| PhiDP_RanGradient_max                        |                                                |             |                                |
| PhiDP_RanGradient_mean                       |                                                |             |                                |
| PhiDP_RanGradient_min                        |                                                |             |                                |
| PhiDP_RanGradient_25th_percentile            |                                                |             |                                |
| PhiDP_RanGradient_median                     |                                                |             |                                |
| PhiDP_RanGradient_75th_percentile            |                                                |             |                                |
| PhiDP_Gradient_max                           |                                                |             |                                |
| PhiDP_Gradient_mean                          |                                                |             |                                |
| PhiDP_Gradient_min                           |                                                |             |                                |
| PhiDP_Gradient_25th_percentile               |                                                |             |                                |
| PhiDP_Gradient_median                        |                                                |             |                                |
| PhiDP_Gradient_75th_percentile               |                                                |             |                                |
| PhiDP_MedianFiltered_max                     |                                                |             |                                |
| PhiDP_MedianFiltered_mean                    |                                                |             |                                |
| PhiDP_MedianFiltered_min                     |                                                |             |                                |
| PhiDP_MedianFiltered_25th_percentile         |                                                |             |                                |
| PhiDP_MedianFiltered_median                  |                                                |             |                                |
| PhiDP_MedianFiltered_75th_percentile         |                                                |             |                                |
| Reflectivity_AzGradient_max                  |                                                |             |                                |
| Reflectivity_AzGradient_mean                 |                                                |             |                                |
| Reflectivity_AzGradient_min                  |                                                |             |                                |
| Reflectivity_AzGradient_25th_percentile      |                                                |             |                                |
| Reflectivity_AzGradient_median               |                                                |             |                                |
| Reflectivity_AzGradient_75th_percentile      |                                                |             |                                |
| Reflectivity_RanGradient_max                 |                                                |             |                                |
| Reflectivity_RanGradient_mean                |                                                |             |                                |
| Reflectivity_RanGradient_min                 |                                                |             |                                |
| Reflectivity_RanGradient_25th_percentile     |                                                |             |                                |
| Reflectivity_RanGradient_median              |                                                |             |                                |
| Reflectivity_RanGradient_75th_percentile     |                                                |             |                                |
| Reflectivity_Gradient_max                    |                                                |             |                                |
| Reflectivity_Gradient_mean                   |                                                |             |                                |
| Reflectivity_Gradient_min                    |                                                |             |                                |
| Reflectivity_Gradient_25th_percentile        |                                                |             |                                |
| Reflectivity_Gradient_median                 |                                                |             |                                |
| Reflectivity_Gradient_75th_percentile        |                                                |             |                                |
| Reflectivity_MedianFiltered_max              |                                                |             |                                |
| Reflectivity_MedianFiltered_mean             |                                                |             |                                |
| Reflectivity_MedianFiltered_min              |                                                |             |                                |
| Reflectivity_MedianFiltered_25th_percentile  |                                                |             |                                |
| Reflectivity_MedianFiltered_median           |                                                |             |                                |
| Reflectivity_MedianFiltered_75th_percentile  |                                                |             |                                |
| RhoHV_AzGradient_max                         |                                                |             |                                |
| RhoHV_AzGradient_mean                        |                                                |             |                                |
| RhoHV_AzGradient_min                         |                                                |             |                                |
| RhoHV_AzGradient_25th_percentile             |                                                |             |                                |
| RhoHV_AzGradient_median                      |                                                |             |                                |
| RhoHV_AzGradient_75th_percentile             |                                                |             |                                |
| RhoHV_RanGradient_max                        |                                                |             |                                |
| RhoHV_RanGradient_mean                       |                                                |             |                                |
| RhoHV_RanGradient_min                        |                                                |             |                                |
| RhoHV_RanGradient_25th_percentile            |                                                |             |                                |
| RhoHV_RanGradient_median                     |                                                |             |                                |
| RhoHV_RanGradient_75th_percentile            |                                                |             |                                |
| RhoHV_Gradient_max                           |                                                |             |                                |
| RhoHV_Gradient_mean                          |                                                |             |                                |
| RhoHV_Gradient_min                           |                                                |             |                                |
| RhoHV_Gradient_25th_percentile               |                                                |             |                                |
| RhoHV_Gradient_median                        |                                                |             |                                |
| RhoHV_Gradient_75th_percentile               |                                                |             |                                |
| RhoHV_MedianFiltered_max                     |                                                |             |                                |
| RhoHV_MedianFiltered_mean                    |                                                |             |                                |
| RhoHV_MedianFiltered_min                     |                                                |             |                                |
| RhoHV_MedianFiltered_25th_percentile         |                                                |             |                                |
| RhoHV_MedianFiltered_median                  |                                                |             |                                |
| RhoHV_MedianFiltered_75th_percentile         |                                                |             |                                |
| SpectrumWidth_AzGradient_max                 |                                                |             |                                |
| SpectrumWidth_AzGradient_mean                |                                                |             |                                |
| SpectrumWidth_AzGradient_min                 |                                                |             |                                |
| SpectrumWidth_AzGradient_25th_percentile     |                                                |             |                                |
| SpectrumWidth_AzGradient_median              |                                                |             |                                |
| SpectrumWidth_AzGradient_75th_percentile     |                                                |             |                                |
| SpectrumWidth_RanGradient_max                |                                                |             |                                |
| SpectrumWidth_RanGradient_mean               |                                                |             |                                |
| SpectrumWidth_RanGradient_min                |                                                |             |                                |
| SpectrumWidth_RanGradient_25th_percentile    |                                                |             |                                |
| SpectrumWidth_RanGradient_median             |                                                |             |                                |
| SpectrumWidth_RanGradient_75th_percentile    |                                                |             |                                |
| SpectrumWidth_Gradient_max                   |                                                |             |                                |
| SpectrumWidth_Gradient_mean                  |                                                |             |                                |
| SpectrumWidth_Gradient_min                   |                                                |             |                                |
| SpectrumWidth_Gradient_25th_percentile       |                                                |             |                                |
| SpectrumWidth_Gradient_median                |                                                |             |                                |
| SpectrumWidth_Gradient_75th_percentile       |                                                |             |                                |
| SpectrumWidth_MedianFiltered_max             |                                                |             |                                |
| SpectrumWidth_MedianFiltered_mean            |                                                |             |                                |
| SpectrumWidth_MedianFiltered_min             |                                                |             |                                |
| SpectrumWidth_MedianFiltered_25th_percentile |                                                |             |                                |
| SpectrumWidth_MedianFiltered_median          |                                                |             |                                |
| SpectrumWidth_MedianFiltered_75th_percentile |                                                |             |                                |
| Vrot                                         |                                                |             |                                |
| Vrot_Distance                                |                                                |             |                                |
| Velocity_Gradient_max                        |                                                |             |                                |
| Velocity_Gradient_mean                       |                                                |             |                                |
| Velocity_Gradient_min                        |                                                |             |                                |
| Velocity_Gradient_25th_percentile            |                                                |             |                                |
| Velocity_Gradient_median                     |                                                |             |                                |
| Velocity_Gradient_75th_percentile            |                                                |             |                                |
| Velocity_MedianFiltered_max                  |                                                |             |                                |
| Velocity_MedianFiltered_mean                 |                                                |             |                                |
| Velocity_MedianFiltered_min                  |                                                |             |                                |
| Velocity_MedianFiltered_25th_percentile      |                                                |             |                                |
| Velocity_MedianFiltered_median               |                                                |             |                                |
| Velocity_MedianFiltered_75th_percentile      |                                                |             |                                |
| Zdr_AzGradient_max                           |                                                |             |                                |
| Zdr_AzGradient_mean                          |                                                |             |                                |
| Zdr_AzGradient_min                           |                                                |             |                                |
| Zdr_AzGradient_25th_percentile               |                                                |             |                                |
| Zdr_AzGradient_median                        |                                                |             |                                |
| Zdr_AzGradient_75th_percentile               |                                                |             |                                |
| Zdr_RanGradient_max                          |                                                |             |                                |
| Zdr_RanGradient_mean                         |                                                |             |                                |
| Zdr_RanGradient_min                          |                                                |             |                                |
| Zdr_RanGradient_25th_percentile              |                                                |             |                                |
| Zdr_RanGradient_median                       |                                                |             |                                |
| Zdr_RanGradient_75th_percentile              |                                                |             |                                |
| Zdr_Gradient_max                             |                                                |             |                                |
| Zdr_Gradient_mean                            |                                                |             |                                |
| Zdr_Gradient_min                             |                                                |             |                                |
| Zdr_Gradient_25th_percentile                 |                                                |             |                                |
| Zdr_Gradient_median                          |                                                |             |                                |
| Zdr_Gradient_75th_percentile                 |                                                |             |                                |
| Zdr_MedianFiltered_max                       |                                                |             |                                |
| Zdr_MedianFiltered_mean                      |                                                |             |                                |
| Zdr_MedianFiltered_min                       |                                                |             |                                |
| Zdr_MedianFiltered_25th_percentile           |                                                |             |                                |
| Zdr_MedianFiltered_median                    |                                                |             |                                |
| Zdr_MedianFiltered_75th_percentile           |                                                |             |                                |