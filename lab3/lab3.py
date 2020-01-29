import arcade

arcade.open_window(800,600, "Drawing Example")
arcade.set_background_color(arcade.color.BLUE)


arcade.start_render()
# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)
# --- Draw the barn ---
# Barn cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)
# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BROWN)
 
# Left-bottom window
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE) 
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BLACK)
# Right-bottom window
#arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.co)
arcade.finish_render()
    
arcade.run()