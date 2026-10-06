def video_views(titles, views):
    return [(title, round(view, -3)) for title, view in zip(titles, views)]


titles = ["Python Tutorial", "AI Explained", "Web Development"]
views = [125430, 78450, 231780]

result = video_views(titles, views)

print(result)