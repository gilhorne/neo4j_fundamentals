# Neo4j has built-in support for two-dimensional and three-dimensional spatial data types. These are referred to as points. A point may represent geographic coordinates (longitude, latitude) or Cartesian coordinates (x, y) 

#Point(Cartesian) = neo4j.spatial.CartesianPoint 
#Point(WGS-84) = neo4j.spatial.WGS84Point
#neo4j.spatial.Point 

# --- CARTESIAN POINTS ---
from neo4j.spatial import CartesianPoint

two_d = CartesianPoint((x,y)) #this will create a 2d point 
three_d = CartesianPoint((x,y,z)) #this will create a 3d point

# The driver will convert point data types created with an x, y and z value to an instance of the CartesianPoint class

records, summary, keys = driver.execute_query("""
RETURN point( {x:1.23, y:4.56, z:7.89}) AS threeD
"""
)

point = records[0]["threeD"]

#Accessing attributes
print(point.x, point.y, point.z, point.srid)

#Destructuring 
x, y, z = point

#values can be accessed by using the x,y,z attributes or by destructuring the point.

# --- WGS-84 POINTS ---
#WGS (World Geodetic System) uses coordinates of longitude and latitude
from neo4j.spatial import WGS84Point

ldn = WGS84Point((-0.118092, 51.509865)) #longitude, latitude
print(ldn.latitude) # Accesses the latitude of a WGS-84 point.
print(ldn.longitude) # Accesses the longitude of a WGS-84 point. 
print(ldn.srid) # Returns the spatial reference system identifier of a point.

shard = WGS84Point((-0.086500, 51.504501, 310)) # x, y and z (height)
print(shard.longitude, shard.latitude, shard.height, shard.srid)

# Using destructuring:
longitude, latitude, height = shard


records, summary, keys = driver.execute_query("""
RETURN point ({
    latitude: 51.5,
    logitude: -0.118,
    height: 100
    }) AS point
""")

point = records[0]["point"]
longitue, latitude, height = point

# --- DISTANCE ---
# point.distance function can calculate the distance between two points with the same SRID:

# Create two points
point_1 = CartesianPoint((1,1))
point_2 = CartesianPoint((10,10))

# Query the distance between the two points:
records, summary, keys = driver.execute_query("""
RETURN point.distane( $p1, $p2) AS distance
""", p1=point_1, p2=point_2)

# Print the distance from the result
distance = records[0]["distance"]
print(distance)
                
# function will return None if SRID values are different