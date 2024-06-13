import movis as mv


def get_video_from_text(text: str):
    if len(text) == 0:
        text = "empty"
    scene_size = (100, 100)
    scene_duration = 3.0
    scene = mv.layer.Composition(size=scene_size, duration=scene_duration)
    scene.add_layer(mv.layer.Rectangle(scene.size, color='#153706'))
    text_layer = mv.layer.Text(text, font_size=52, font_family='Sans Serif', color='#706153')
    start_pos = scene.size[0] + text_layer.get_size()[0] // 2, scene.size[1] // 2
    end_pos = - text_layer.get_size()[0] // 2, scene.size[1] // 2
    scene.add_layer(
        text_layer,
        name='text',
        position=start_pos,
        anchor_point=(0.0, 0.0),
        opacity=1.0, scale=1.0, rotation=0.0,
        blending_mode='normal')
    scene['text'].position.enable_motion().extend(
        keyframes=[0.0, 2.0], values=[start_pos, end_pos], easings=['ease_in_out'])
    scene.write_video(f"media/videos/{text}.mp4")
    return {'name': text, 'path': f"videos/{text}.mp4"}
