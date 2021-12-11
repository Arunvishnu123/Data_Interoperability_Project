package JSON_Objects_Creation;
import com.fasterxml.jackson.databind.*;

public class JSON_Java_Objects 


{
	
	
	public static void main(String[]  st) {
		
		String jsonstr = "{\r\n"
				+ "\"emp_id\":1,\r\n"
				+ "\"name\":\"Arun\",\r\n"
				+ "\"cmpName:\"Rockwell\"\r\n"
				+ "\r\n"
				+ "}";
		
		ObjectMapper mapper = new ObjectMapper();
		mapper.readValue(jsonstr,employee.class)
		
	}
+
}
