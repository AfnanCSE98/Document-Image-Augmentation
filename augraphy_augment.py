import random
from augraphy import *
import cv2
import numpy as np
import sys


def badPhotocopy(img):
    BadPhotoCopy_type_1 = BadPhotoCopy(noise_type=1,
                                    noise_side="left",
                                    noise_iteration=(2,3),
                                    noise_size=(2,3),
                                    noise_sparsity=(0.15,0.15),
                                    noise_concentration=(0.3,0.3),
                                    blur_noise=-1,
                                    blur_noise_kernel=(5, 5),
                                    wave_pattern=0,
                                    edge_effect=0)
    img_BadPhotoCopy_type_1 = BadPhotoCopy_type_1(img)
    # cv2.imshow("type1",img_BadPhotoCopy_type_1)
    cv2.imwrite("./"+output_dir + "/badphotocopy-" + fname.split('.')[0] + ".jpg", img_BadPhotoCopy_type_1)

def bindings(img):
    binder_punch_holes = BindingsAndFasteners(overlay_types="darken",
                                    foreground=None,
                                    effect_type="punch_holes",
                                    ntimes=(3, 3),
                                    nscales=(1.5, 1.5),
                                    edge="left",
                                    edge_offset=(30,50),
                                    use_figshare_library=1,
                                )

    img_punch_holes =binder_punch_holes(img)
    cv2.imwrite("./"+output_dir + "/bindings-" + fname.split('.')[0] + ".jpg", img_punch_holes)

def bleedThrough(img):
    bleedthrough = BleedThrough(intensity_range=(0.1, 0.2),
                            color_range=(0, 224),
                            ksize=(17, 17),
                            sigmaX=0,
                            alpha=0.3,
                            offsets=(10, 20),
                        )

    img_bleedthrough = bleedthrough(img)
    cv2.imwrite("./"+output_dir + "/bleedthrough-" + fname.split('.')[0] + ".jpg", img_bleedthrough)

def bookbinding(img):
    book_binder_up = BookBinding(radius_range=(50, 100),
                        curve_range=(200, 300),
                        mirror_range=(0.2, 0.3),
                        curling_direction=0,
                        )

    img_book_binding_up= book_binder_up(img)
    cv2.imwrite("./"+output_dir + "/bookbinding-" + fname.split('.')[0] + ".jpg", img_book_binding_up)

def brightnesstexture(img):
    brightness_texturize = BrightnessTexturize(texturize_range=(0.9, 0.99),
                                           deviation=0.1 )

    img_brightness_texturize = brightness_texturize(img)
    cv2.imwrite("./"+output_dir + "/brightness-texturize-" + fname.split('.')[0] + ".jpg", img_brightness_texturize)

def dirtDrum1(img):
    dirtydrum1 = DirtyDrum(line_width_range=(1, 4),
                      line_concentration=0.1,
                      direction=0,
                      noise_intensity=0.5,
                      noise_value=(0, 30),
                      ksize=(3, 3),
                      sigmaX=0,
                      )

    img_dirtydrum1 = dirtydrum1(img)
    cv2.imwrite("./"+output_dir + "/dirt-drum1-" + fname.split('.')[0] + ".jpg", img_dirtydrum1)

def dirtyDrum2(img):
    dirtydrum2 = DirtyDrum(line_width_range=(5, 10),
                      line_concentration=0.3,
                      direction=1,
                      noise_intensity=0.2,
                      noise_value=(0, 10),
                      ksize=(3, 3),
                      sigmaX=0,
                      )

    img_dirtydrum2 = dirtydrum2(img)
    cv2.imwrite("./"+output_dir + "/dirt-drum2-" + fname.split('.')[0] + ".jpg", img_dirtydrum2)

def dirtyRollers(img):
    dirty_rollers = DirtyRollers(line_width_range=(12, 25),
                            scanline_type=0,
                            )

    img_dirty_rollers = dirty_rollers(img)
    cv2.imwrite("./"+output_dir + "/dirt-rollers-" + fname.split('.')[0] + ".jpg", img_dirty_rollers)

def folding(img):
    folding = Folding(fold_count=4,
                  fold_noise=0.1,
                  gradient_width=(0.1, 0.2),
                  gradient_height=(0.01, 0.1)
                  )

    img_folded= folding(img)
    cv2.imwrite("./"+output_dir + "/folding-" + fname.split('.')[0] + ".jpg", img_folded)

def lightingGradient(img):
    lighting_gradient_gaussian = LightingGradient(light_position=None,
                                              direction=90,
                                              max_brightness=255,
                                              min_brightness=0,
                                              mode="gaussian",
                                              transparency=0.5
                                              )

    img_lighting_gradient_gaussian = lighting_gradient_gaussian(img)
    cv2.imwrite("./"+output_dir + "/lighting-gradient-gaussian-" + fname.split('.')[0] + ".jpg", img_lighting_gradient_gaussian)

#doesn't work much
def markupStrikethrough(img):
    markup_strikethrough = Markup(num_lines_range=(5, 7),
                              markup_length_range=(0.5, 1),
                              markup_thickness_range=(1, 2),
                              markup_type="strikethrough",
                              markup_color=(0, 0, 255),
                              repetitions=4,
                              single_word_mode=True)

    img_markup_strikethrough = markup_strikethrough(img)
    cv2.imwrite("./"+output_dir + "/markup-strikethrough-" + fname.split('.')[0] + ".jpg", img_markup_strikethrough)

def markupHighlight(img):
    markup_highlight = Markup(num_lines_range=(1, 1),
                          markup_length_range=(0.5, 1),
                          markup_thickness_range=(1, 2),
                          markup_type="highlight",
                          markup_color=(0, 255, 0),
                          repetitions=1,
                          single_word_mode=False)

    img_markup_highlight = markup_highlight(img)
    cv2.imwrite("./"+output_dir + "/markup-highlight-" + fname.split('.')[0] + ".jpg", img_markup_highlight)

#doesn't work much
def markupUnderline(img):
    markup_underline = Markup(num_lines_range=(1, 1),
                          markup_length_range=(0.5, 1),
                          markup_thickness_range=(1, 2),
                          markup_type="underline",
                          markup_color=(255, 0, 0),
                          repetitions=1,
                          single_word_mode=False)

    img_markup_underline = markup_underline(img)
    cv2.imwrite("./"+output_dir + "/markup-underline-" + fname.split('.')[0] + ".jpg", img_markup_underline)

def pageBorder(img):
    page_border = PageBorder(side="random",
                         border_background_value = (230,255),
                         flip_border = 0,
                         width_range=(40, 80),
                         pages=4,
                         noise_intensity_range=(0.4, 0.5),
                         curve_frequency = (4, 8),
                         curve_height = (2, 4),
                         curve_length_one_side = (50, 100),
                         value=(30, 120),
                         same_page_border=0,
                            )
                                
    img_page_border = page_border(img)
    cv2.imwrite("./"+output_dir + "/page-border-" + fname.split('.')[0] + ".jpg", img_page_border)

def pencilScrible(img):
    pencil_scribbles = PencilScribbles(size_range=(400, 800),
                                   count_range=(2, 3),
                                   stroke_count_range=(1, 1),
                                   thickness_range=(1, 3),
                                   brightness_change=128
                                   )

    img_pencil_scribbles = pencil_scribbles(img)
    cv2.imwrite("./"+output_dir + "/pencil-scribbles-" + fname.split('.')[0] + ".jpg", img_pencil_scribbles)

# start main
if __name__ == "__main__":

    fname = sys.argv[1]
    img = cv2.imread(fname)
    output_dir = sys.argv[2]

    # call the augmentation functions
    # brightnesstexture(img)
    dirtDrum1(img)
    dirtyDrum2(img)
    dirtyRollers(img)
    folding(img)
    lightingGradient(img)
    # pageBorder(img)
    pencilScrible(img)
    markupHighlight(img)
    badPhotocopy(img)
    bindings(img)
    bleedThrough(img)
    # bookbinding(img)
    
    
