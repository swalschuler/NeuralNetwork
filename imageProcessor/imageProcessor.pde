void setup()
{
  PImage img;
  String shape = "c";
  String num = "1";
  img = loadImage("../newImages/" + shape + num + ".png");
  image(img, 0, 0);
  
  img.loadPixels();
  
  PrintWriter output = createWriter(shape + num + ".txt");
  if (shape == "c")
    output.println("0");
  else
    output.println("1");
  for (int y = 0; y < img.height; y++)
  {
    String row = "";
    for (int x = 0; x < img.width; x++)
    {
      int index = (y * img.width) + x; 
      float r = red(img.pixels[index]);
      float g = green(img.pixels[index]);
      float b = blue(img.pixels[index]);
      
      if ((r + g + b) / 3 == 0)
        row += "0";
      else
        row += "1";
    }
    output.println(row);
  }
  
  output.flush();
  output.close();
  exit();
}