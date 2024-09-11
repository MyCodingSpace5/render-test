import math

import raytracingtest


class Ray:
    deriative: int
    direction: [int]
    hit: bool
    actualdirection: [int]
class Camera:
    Raything: Ray
    center: float

    def __init__(self, angle: int):
        self.center = math.radians(angle)
        self.Raything = Ray()
        return self


def ray(angle: int) -> None:
    angle = math.radians(angle)
    b: Ray = Ray()
    dir = [math.cos(angle), math.sin(angle)]
    b.direction = dir
    b.deriative = math.tan(angle) # Tangent is depth or z in this case, since it is the deriative of the angle
    b.actualdirection[0] = math.cos(angle) # Sin and cos are the deriatives of x and y, and are converted to their respective linear counterparts
    b.actualdirection[1] = -math.sin(angle)
def scalarfunction(Ray: Ray, Camera: Camera) -> None:
    raytan = 1 / math.exp(Ray.deriative / Camera.center)
    raycos = 1 / math.exp(Ray.actualdirection[0] / Camera.center)
    raysin = 1 / math.exp(Ray.actualdirection[1] / Camera.center)
    return raytan, raycos, raysin

def main() -> None:
    Ray: raytracingtest.Ray = None
    try:
        assert(Ray != None)
    except(AssertionError):
        print("Ray is not initialized")
def plot() -> None:
    pass

if __name__ == "__main__":
    main()

