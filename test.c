#include<stdio.h>
#include<stdlib.h>

#define IMG_PATH 'C:\Users\hsin\Desktop\pic_500\lay0.jpg'

void downsample (uint8_t * input_image, uint32_t input_width, uint32_t input_height, uint8_t * output_image, uint32_t output_width, uint32_t output_height)
{
    uint32_t input_ptr_index1 = 0;
    uint32_t input_ptr_index2 = 0;
    uint32_t input_ptr_index3 = 0;
    uint32_t output_ptr_index1 = 0;
    uint32_t output_ptr_index2 = 0;
    uint32_t width_step = 0;
    uint32_t height_step = 0;

    uint32_t width_i1 = 0;
    uint32_t height_i1 = 0;
    uint32_t width_i2 = 0;
    uint32_t height_i2 = 0;
    uint32_t pixel_buf = 0;
        
    width_step = input_width / output_width; 
    height_step = input_height / output_height; 


    //printf("input height %3d, width = %3d\n", input_height, input_width);
    //printf("output height %3d, width = %3d\n", output_height, output_width);
    //printf("step height %3d, input index = %d\n", height_step, width_step);

    for(height_i1 = 0; height_i1 < output_height; height_i1 ++)
    {
        output_ptr_index1 = height_i1 * output_width;
        for(width_i1 = 0; width_i1 < output_width; width_i1 ++)
        {
            pixel_buf = 0;    
            input_ptr_index1 = (height_i1 * height_step * input_width) + (width_i1 * width_step);   
            for(height_i2 = 0; height_i2 < height_step; height_i2 ++)
            {
                input_ptr_index2 = height_i2 * input_width;
                for(width_i2 = 0; width_i2 < width_step; width_i2 ++)
                {
                    input_ptr_index3 = input_ptr_index1 + input_ptr_index2 + width_i2;
                    pixel_buf = pixel_buf + *(input_image + input_ptr_index3);
                }
            }
            output_ptr_index2 = output_ptr_index1 + width_i1;
            pixel_buf = pixel_buf / (width_step * height_step);
            if(pixel_buf > 255)
                pixel_buf = 255;
            *(output_image + output_ptr_index2) = pixel_buf;
        }
    }
}


int main() {
int output_image[96][96] = {0};
// downsample(IMG_PATH,640,480,output_image,96,96);
printf("%d",IMG_PATH);
return 0;
}