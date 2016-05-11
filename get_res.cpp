#include <hd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *file = fopen("/var/lib/mandriva/kde4-profiles/common/share/config/kcm-modes", "w");
    hd_data_t hd_data;
    memset(&hd_data, 0, sizeof(hd_data));
    hd_t *hd = hd_list(&hd_data, hw_framebuffer, 1, NULL);
    if(hd)
    {
       for (hd_res_t *res = hd->res; res; res = res->next) {
          if (res->any.type == res_framebuffer) {
    	    fprintf(file, "%dx%dx%d\n", res->framebuffer.width, res->framebuffer.height, res->framebuffer.colorbits);
          }
       }
       hd_free_hd_list(hd);
       hd_free_hd_data(&hd_data);
    }
    fclose(file);
    return 0;
}
