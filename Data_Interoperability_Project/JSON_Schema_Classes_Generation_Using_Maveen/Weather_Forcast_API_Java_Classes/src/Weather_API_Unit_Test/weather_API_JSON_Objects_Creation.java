package Weather_API_Unit_Test;
import Weather_API_Classes.WeatherAirConditions;
import Weather_API_Classes.WeatherApi;
import Weather_API_Classes.WeatherCommons;

public class weather_API_JSON_Objects_Creation  {
	
	public static void main(String[] args) {
		
	WeatherAirConditions weatherAirCondition = new WeatherAirConditions();
	weatherAirCondition.setTemperature((double) 2.3);
	weatherAirCondition.setFeelLikesTemperature(1.5);
	weatherAirCondition.setRelativeHumidity(2.1);
	
	weatherAirCondition.getTemperature();
	weatherAirCondition.getFeelLikesTemperature();
	weatherAirCondition.getRelativeHumidity();
	System.out.println(weatherAirCondition);
	
	WeatherApi weatherDetails = new  WeatherApi();
	weatherDetails.setLocation("Saint-Etienne");
	
	weatherDetails.getLocation();
	weatherDetails.getAlert();
	weatherDetails.getDate();
	weatherDetails.getCurrent();
	weatherDetails.getDayMaximum();
	weatherDetails.getDayMinimum();
	System.out.println(weatherDetails);
	
	WeatherCommons weatherCommon = new WeatherCommons();
	
	weatherCommon.setTemperature(4.3);
	weatherCommon.setFeelLikesTemperature(3.2);
	weatherCommon.setRelativeHumidity(1.1);
	weatherCommon.setWeatherType("snowy");
	weatherCommon.setWindDirection(1);
	weatherCommon.setWindSpeed(10.0);
	weatherCommon.setRefPointOfInterest("test");
	
	weatherCommon.getTemperature();
	weatherCommon.getFeelLikesTemperature();
	weatherCommon.getRelativeHumidity();
	weatherCommon.getWeatherType();
	weatherCommon.getVisibility();
	weatherCommon.getWindDirection();
	weatherCommon.getWindSpeed();
	weatherCommon.getRefPointOfInterest();
	System.out.println(weatherCommon);
	}    
	
	
}
