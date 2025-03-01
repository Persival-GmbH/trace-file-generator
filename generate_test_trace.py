from osi3.osi_sensorview_pb2 import SensorView
import struct
import lzma

#f = lzma.open("output.lzma", "ab")
f = lzma.open("output.osi", "ab")
sensorview = SensorView()

sv_ground_truth = sensorview.global_ground_truth
sv_ground_truth.version.version_major = 3
sv_ground_truth.version.version_minor = 0
sv_ground_truth.version.version_patch = 0

sv_ground_truth.timestamp.seconds = 0
sv_ground_truth.timestamp.nanos = 0
sv_ground_truth.host_vehicle_id.value = 113

moving_object = sv_ground_truth.moving_object.add()
moving_object.id.value = 114

# Generate 10 OSI messages for 9 seconds
for i in range(10):
    # Increment the time
    sensorview.timestamp.seconds += 1
    sv_ground_truth.timestamp.seconds += 1

    moving_object.vehicle_classification.type = 2

    moving_object.base.dimension.length = 5
    moving_object.base.dimension.width = 2
    moving_object.base.dimension.height = 1

    moving_object.base.position.x = 0.0 + i
    moving_object.base.position.y = 0.0
    moving_object.base.position.z = 0.0

    moving_object.base.orientation.roll = 0.0
    moving_object.base.orientation.pitch = 0.0
    moving_object.base.orientation.yaw = 0.0

    """Serialize"""
    bytes_buffer = sensorview.SerializeToString()
    f.write(struct.pack("<L", len(bytes_buffer)) + bytes_buffer)

f.close()

