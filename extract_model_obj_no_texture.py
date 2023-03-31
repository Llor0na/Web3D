import struct 

indexCount = 139836
indexTypeSize = 2
wireCount = 279672
vertexCount = 24919
stride = 32
offset = 0

with open("scene/mesh0.dat", 'rb') as f:
    indexBuffer = f.read(indexCount * indexTypeSize)
    f.seek(wireCount * indexTypeSize, 1)
    vertexBuffer = f.read(vertexCount * stride)

with open("mesh0.obj", 'w') as obj:
    for i in range(vertexCount):
        x, y, z = struct.unpack_from("fff", vertexBuffer, stride * i)
        obj.write("v {} {} {}\n".format(x, y, z))

        u, v = struct.unpack_from("ff", vertexBuffer, offset + stride * i)
        obj.write("vt {} {}\n".format(u, v))

    triangleCount = indexCount // 3
    for i in range(triangleCount):
        v0, v1, v2 = struct.unpack_from("HHH", indexBuffer, 3 * indexTypeSize * i)
        obj.write("f {}/{} {}/{} {}/{}\n".format(v0 + 1, v0 + 1, v1 + 1, v1 + 1, v2 + 1, v2 + 1))