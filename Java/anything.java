import java.io.*; 
import java.net.*; 
  
class pinga { 
  // Sends ping request to a provided IP address 
  public static void sendPingRequest(String ipAddress) throws UnknownHostException, IOException { 
    InetAddress main = InetAddress.getByName(ipAddress); 
    if (main.isReachable(5000)){
      System.out.println("Feito"); 
    } 
    else{
      System.out.println("Deu Ruim"); 
    }
  } 
  
  // Driver code 
  public static void main(String[] args) throws UnknownHostException, IOException { 
    String ipAddress = "192.168.9.20"; 
    sendPingRequest(ipAddress); 
  } 
} 