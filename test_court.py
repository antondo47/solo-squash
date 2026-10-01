# to test the court

from court import build_homography, make_pixel_to_court

pixel_points = [(367, 374), (313, 466), (984, 372), (1052, 463)]
court_points = [(0.00, 5.49), (0.00, 7.09), (6.40, 5.49), (6.40, 7.09)]

H = build_homography(pixel_points, court_points)
to_court = make_pixel_to_court(H)

for (px, py), (ex, ey) in zip(pixel_points, court_points):
    gx, gy = to_court(px, py)
    print(f"({px},{py}) -> ({gx:.2f}, {gy:.2f})   expect ({ex}, {ey})")