package com.londonappbrewery.climapm;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SearchRecentSuggestionsProvider;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.telecom.Call;
import android.util.Log;
import android.view.View;
import android.view.accessibility.AccessibilityRecord;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.json.JSONObject;

import cz.msebera.android.httpclient.Header;


public class WeatherController extends AppCompatActivity {

    // Constants:
    final int REQUEST_CODE = 123;  // id for the location change runtime permission request
    final String WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather";
    // App ID to use OpenWeather data
    final String APP_ID = "290cda55270f750752e1ffdedbf1ef56";
    // Time between location updates (5000 milliseconds or 5 seconds)
    final long MIN_TIME = 5000;
    // Distance between location updates (1000m or 1km)
    final float MIN_DISTANCE = 1000;

    // TODO: Set LOCATION_PROVIDER here:
    String LOCATION_PROVIDER = LocationManager.GPS_PROVIDER;


    // Member Variables:
    TextView mCityLabel;
    TextView mTemperatureLabel;
    ImageView mWeatherImage;

    // TODO: Declare a LocationManager and a LocationListener here:
    LocationManager mLocationManager;  // to start & stop requesting location updates
    LocationListener mLocationListener;  // notified if the location has changed


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.weather_controller_layout);

        // Linking the elements in the layout to Java code
        mCityLabel = findViewById(R.id.locationTV);
        mWeatherImage = findViewById(R.id.weatherSymbolIV);
        mTemperatureLabel = findViewById(R.id.tempTV);
        ImageButton changeCityButton = findViewById(R.id.changeCityButton);



        // TODO: Add an OnClickListener to the changeCityButton here:
        changeCityButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Create an Intent for this button to change to the change city activity.
                Intent myIntent = new Intent(WeatherController.this, ChangeCityController.class);
                startActivity(myIntent);
            }
        });

    }


    // TODO: Add onResume() here:
    @Override
    protected void onResume() {
        super.onResume();
        Log.d("Clima", "onResume() called");
        Log.d("Clima", "Getting weather for current location");

        // Retrieve the intent here because onResume is triggered when an activity become active
        Intent myIntent = getIntent();

        // Retrieve the extra inside the intent
        String city = myIntent.getStringExtra("City");

        if (city != null) {
            getWeatherForNewCity(city);

        } else {

            // method to get weather for current location
            getWeatherForCurrentLocation();

        }
    }

    // TODO: Add getWeatherForNewCity(String city) here:
    private void getWeatherForNewCity(String city) {

        // Create a requestparams object with the weather request data for the new city
        RequestParams newCityParams = new RequestParams();
        newCityParams.put("q", city);
        newCityParams.put("appid", APP_ID);

        // Call method to make weather request for new city
        letsDoSomeNetworking(newCityParams);

    }


    // TODO: Add getWeatherForCurrentLocation() here:
    private void getWeatherForCurrentLocation() {
        mLocationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);

        // Initialize a location change listener
        mLocationListener = new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                Log.d("Clima", "onLocationChanged() callback received");

                // Fetch the location details passed back to our code by the componenet triggering
                // the location change event (The details are in the 'location' object passed into this method
                // from the listener

                String longitude = String.valueOf(location.getLongitude());
                String latitude = String.valueOf(location.getLatitude());

                Log.d("Clima", "Longitude: " + longitude);
                Log.d("Clima", "Latitude: " + latitude);

                // From James Smiths networking library allowing us to make HTTP request, create a requet variable that willhold the request data:
                RequestParams params = new RequestParams();
                params.put("lat", latitude);
                params.put("lon", longitude);
                params.put("appid", APP_ID);

                // Call method to make request
                letsDoSomeNetworking(params);
            }

            @Override
            public void onStatusChanged(String s, int i, Bundle bundle) {

            }

            @Override
            public void onProviderEnabled(String s) {

            }

            @Override
            public void onProviderDisabled(String s) {
                Log.d("Clima", "onProviderDisabled() callback received");
            }
        };

        // For below request to work, user permission to fetch location must be sought at runtime and logic be in place to handle acceptance or rejection by the user. Implement runtime permission request before starting to request for location updates.

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {

            // Request permission
            ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, REQUEST_CODE);

            return;
        }

        // Start getting location updates
        mLocationManager.requestLocationUpdates(LOCATION_PROVIDER, MIN_TIME, MIN_DISTANCE, mLocationListener);

    }

    // Method callback to get the user response from the OS for the location update retrival permission request. Insert using Android Studio > right click and select generate, pick from pop up

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        // Check the request id matches ours (the same as supplied when we made the request
        if (requestCode == REQUEST_CODE) {
            // Check that the response array is not empty and that permission granted is the first element in it.
            if (grantResults.length >0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                Log.d("Clima", "onRequestPermissionsResult(): Permission granted");
                getWeatherForCurrentLocation();

            } else {
                Log.d("Clima", "Permission denied");
            }
        }

    }


    // TODO: Add letsDoSomeNetworking(RequestParams params) here:
    private void letsDoSomeNetworking(RequestParams params) {

        // Initialize an AsyncHttpClient object that will be used to make HTTP requests asynchronously (as other task continue, especially those involving UI interactions, so that the app remains responsive as it waits fro feedback from the request)
        AsyncHttpClient client = new AsyncHttpClient();

        // Make a GET request
        client.get(WEATHER_URL, params, new JsonHttpResponseHandler() {
            // The object from the JsonHttpResponseHandler class, also part of Jame's library, will receive either a fail or success response, which we will deal with it's bodym herein

            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                Log.d("Clima", "Success! " + response.toString());

                // Instantiate the WeatherDataModel class
                WeatherDataModel weatherdata = WeatherDataModel.fromJson(response);

                // Call the updateUI method
                updateUI(weatherdata);

            }

            @Override
            public void onFailure(int statusCode, Header[] headers, Throwable e, JSONObject response) {
                Log.e("Clima", "Failure: " + e.toString());
                Log.d("Clima", "Status Code: " + statusCode);
                Toast.makeText(WeatherController.this, "Request Failed", Toast.LENGTH_LONG).show();
            }

        });

    }


    // TODO: Add updateUI() here:
    private void updateUI (WeatherDataModel weather) {

        mCityLabel.setText(weather.getCity());
        mTemperatureLabel.setText(weather.getTemperature());

        int resourceID = getResources().getIdentifier(weather.getIconName(), "drawable", getPackageName());
        mWeatherImage.setImageResource(resourceID);

    }


    // TODO: Add onPause() here:
    // Stop receiving location updates from the location listener when the app the user is not interacting
    // with the app to save device resources e.g battery

    // Override the onPause method and add code to check if the Location manager has location values, then stop
    // listening for location updates

    @Override
    protected void onPause() {
        super.onPause();
        if (mLocationManager != null) {
            mLocationManager.removeUpdates(mLocationListener);
        }

        // Also: if (mLocationManager != null) mLocationManager.removeUpdates(mLocationListener);
    }
}
