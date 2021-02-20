types = {
    "root_list": {
        1: ("day_session"),
    },
    "day_session": {
        1: ("string", "session_uuid"),
        2: ("int32"),
        3: ("sfixed64", "main_timestamp"),
        4: ("string", "location_name"),
        5: ("location_list"),
    },
    "location_list": {
        2: ("gps_location"),
    },
    "gps_location": {
        1: ("sfixed64", "timestamp"),
        2: ("double", "x"),
        3: ("double", "y"),
        4: ("double", "z")
    }
}
