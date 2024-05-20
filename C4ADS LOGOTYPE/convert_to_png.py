from PIL import Image
import os

def convert_eps_to_png(eps_path, png_path):
    image = Image.open(eps_path)
    image.load(scale=10)  # Increase scale to improve resolution
    image.save(png_path, 'PNG')

def main():
    logos = [
        'C4ADS_Logotype-NOtagline_FINAL_Black.eps',
        'C4ADS_Logotype-NOtagline_FINAL_White.eps',
        'C4ADS_Logotype-tagline_FINAL_Black.eps',
        'C4ADS_Logotype-tagline_FINAL_White.eps'
    ]
    
    for logo in logos:
        eps_path = os.path.join('logoless', logo)
        png_path = os.path.join('logoless', os.path.splitext(logo)[0] + '.png')
        convert_eps_to_png(eps_path, png_path)
        print(f"Converted {eps_path} to {png_path}")

if __name__ == "__main__":
    main()
