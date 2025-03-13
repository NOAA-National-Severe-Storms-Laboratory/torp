
## Description of TORP Dataset  

| **Field**        | **Description**                                           | **Unit**    | **Format / Example**                    |
|:-----------------|:----------------------------------------------------------|:------------|:----------------------------------------|
| timestamp        | Valid time of the data entry                              | \-          | String `YYYYMMDD-hhmm` (e.g., `20240305-1530`) |
| year             | Calendar year                                             | \-          | String `YYYY` (e.g., `2024`)            |
| month            | Calendar month                                            | \-          | String `MM` (e.g., `03`)                |
| day              | Calendar day                                              | \-          | String `DD` (e.g., `05`)                |
| time             | Time in hours/minutes                                     | \-          | String `HHmm` (e.g., `0530`)            |
| unixTime         | Seconds since **January 1, 1970** (Unix epoch)            | s           | Integer (e.g., `1709637000`)            |
| latitude         | Geographic latitude                                       | °           | Decimal (e.g., `35.6789`)               |
| longitude        | Geographic longitude (negative for W)                     | °           | Decimal (e.g., `-97.1234`)              |
| radar            | 4-letter radar station identifier (ICAO)                  | \-          | String (e.g., `KTLX`)                   |
| rangeKm          | Distance to the nearest (dual-pol) radar                  | km          | Float (e.g., `34.5`)                    |
| beginTimestamp   | Report start time                                         | \-          | String `YYYYMMDD-hhmm` (e.g., `20240305-1530`) |
| beginYear        | Report start year                                         | \-          | String `YYYY` (e.g., `2024`)            |
| beginMonth       | Report start month                                        | \-          | String `MM` (e.g., `03`)                |
| beginDay         | Report start day                                          | \-          | String `DD` (e.g., `05`)                |
| beginTime        | Report start time in                                      | \-          | String`HHmm` (e.g., `0530`)             |
| beginUnix        | Report start time in seconds since January 1, 1970 (Unix epoch) | s           | Integer (e.g., `1709637000`)      |
| beginLongitude   | Report start geographic latitude                          | °           | Float (e.g., `35.6789`)                 |
| beginLatitude    | Report start geographic longitude (negative for W)        | °           | Float (e.g., `-97.1234`)                |
| endTimestamp     | Report end time                                           | \-          | String `YYYYMMDD-hhmm` (e.g., `20240305-1530`)   |
| endYear          | Report end year                                           | \-          | String `YYYY` (e.g., `2024`)                     |
| endMonth         | Report end month                                          | \-          | String `MM` (e.g., `03`)                         |
| endDay           | Report end day                                            | \-          | String `DD` (e.g., `05`)                         |
| endTime          | Report end time in                                        | \-          | String `HHmm` (e.g., `0530`)                     |
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
| type                              | `Non-Severe`, `Severe Non-Tornadic`, `Significant Severe Non-Tornadic`, `Waterspout`, `Landspout`, `Tornado`, `Significant Tornado` | \-          | String |
| tornadoLength    | From Storm Data: Length of the tornado or tornado segment while on the ground.  | mi          | Float    |
| tornadoWidth     | From Storm Data: Width of the tornado or tornado segment while on the ground.   | yd          | Integer  |
| injuriesDirect   | From Storm Data: The number of injuries directly caused by the weather event.   | people      | Integer  |
| injuriesIndirect | From Storm Data: The number of injuries indirectly caused by the weather event. | people      | Integer  |
| deathsDirect     | From Storm Data: The number of deaths directly caused by the weather event.     | people      | Integer  |
| deathsIndirect   | From Storm Data: The number of deaths indirectly caused by the weather event.   | people      | Integer  |
| damageProperty   | From Storm Data: The estimated amount of damage to property incurred by the weather event. | $           | Integer |
| damageCrops      | From Storm Data: The estimated amount of damage to crops incurred by the weather event.    | $           | Integer |
| source           | From Storm Data: The source reporting the weather event (can be any entry; isn’t restricted in what’s allowed). |             | String (e.g., : `Public`, `Law Enforcement`, `Trained Spotter`, `CoCoRaHS` |
| overview                          | From Storm Data: The episode narrative depicting the general nature and overall activity of the episode. The National Weather Service creates the narrative. | \-          | String |
| details                           | From Storm Data: The event narrative provides descriptive details of the individual event. The National Weather Service creates the narrative. | \-          | String |
| stormEventsEpisodeID              | From Storm Data: ID assigned by NWS to denote the storm episode; Episodes may contain multiple Events. The occurrence of storms and other significant weather phenomena having sufficient intensity to cause loss of life, injuries, significant property damage, and/or disruption to commerce. | \-          | Integer |
| stormEventsReportID               | From Storm Data: ID assigned by NWS for each individual storm event contained within a storm episode. | \-          | Integer |
| oneTorID                          | Common ID for all segments of a tornado. Same as the first segment's stormEventsReportID. Code finds start and end points within one minute and 1 km of one another. | \-          | Integer |
| multiSegment                      | Binary flag for whether a tornado has more than one segment.   | \-          | Boolean/Integer (`1` or `0`) |
| previousSegment                   | The stormEventsReportID of the previous segment in a tornado.  | \-          | Integer                      |
| totalDurationMin                  | Duration for the full tornado track.                           | min         | Integer                      |
| maxMagnitudeAcrossSeg             | Maximum EF rating for the full tornado track.                  | EF          | Integer                      |
| totalTornadoLength                | Sum of the tornado lengths for the full tornado track.         | mi          | Float                        |
| maxTornadoWidth                   | Max of the tornado widths for the full tornado track.          | yd          | Integer                      |
| totalInjuriesDirect               | Sum of the direct injuries lengths for the full tornado track. | people      | Integer                      |
| totalInjuriesIndirect             | Sum of the indirect injuries for the full tornado track.       | people      | Integer                      |
| totalDeathsDirect                 | Sum of the direct deaths for the full tornado track.           | people      | Integer                      |
| totalDeathsIndirect               | Sum of the indirect deaths for the full tornado track.         | people      | Integer                      |
| totalDamageProperty               | Sum of the property damage for the full tornado track.         | $           | Integer                      |
| totalDamageCrops                  | Sum of the crop damage for the full tornado track.             | $           | Integer                      |
| preTornadoTracked                 | Binary flag for whether a tornado was tracked in the pre-tornadic period.   | \-          | Boolean/Integer (`1` or `0`) |
| stormID                           | ID for tornadic storms.                                        | \-          | String `YYYYMM-[first tornado ID]` |
| stormType                         | Manually labled storm mode. Discrete storms could be either supercells or ordinary storms. | \-             | String `Supercell`, `Linear`, `Ordinary`, `TC`, `Discrete` |
| county                            | From Storm Data: County/Parish, Zone or Marine Name assigned to the county FIPS number or NWS Forecast Zone.  | \-          | String |
| state                             | From Storm Data: The state name where the event occurred.      | \-          | String                       |
| CWA                               | From Storm Data: The National Weather Service Forecast Office’s area of responsibility (County Warning Area) in which the event occurred. |             |                                |
| NWSRegion                         |                                                           | \-          | String (`CR`, `ER`, `SR`, or ``) |
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
