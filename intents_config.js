intents_config = {
  "social_media_username_apps":{
    "input":{
      "social_media_username":"string_that_gets_replaced_with_social_media_username"
    },
    "applications":{
      "Twitter":{
        "call_url":"http://twitter.com/string_that_gets_replaced_with_social_media_username",
        "icon":"logos/Twitter_logo_png-4.png"
      },
      "Facebook":{
        "call_url":"http://facebook.com/string_that_gets_replaced_with_social_media_username",
        "icon":"logos/facebook-logo.jpg"
      },
      "Github":{
        "call_url":"http://github.com/string_that_gets_replaced_with_social_media_username",
        "icon":"logos/github-logo.png"
      }
    }
  },
  "geo_text_location_apps":{
    "input":{
      "location":"string_that_gets_replaced_with_location"
    },
    "applications":{
      "Google Maps":{
        "call_url":"http://maps.google.com/?q=string_that_gets_replaced_with_location",
        "icon":"logos/google-maps-logo.jpg"
      },
      "Another App":{
        "call_url":"http://maps.google.com/?q=string_that_gets_replaced_with_location",
        "icon":"logos/google-maps-logo.jpg"
      }
    }
  }
};
