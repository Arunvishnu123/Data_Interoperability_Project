package Java_Object_to_JSON_Creation;
import com.fasterxml.jackson.databind.ObjectMapper;

import JSON_Objects_Creation.employee;
public class Object_JSON_Creation {

	
	
public static void main(String[]  st) {
		
	set_employee employee =new  set_employee(23,"Arun","Rockwell");
	
	ObjectMapper mapper = new ObjectMapper();
	
	String jsonstr = mapper.writeValueAsString(employee);
}
}