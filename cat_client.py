import cat_pb2_grpc
import cat_pb2
import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        local_stub = cat_pb2_grpc.CatsStub(channel)
        print("1. Meow")
        choice = str(input("Which RPC call would you like to make? "))

        if choice == "1":
            cat_request = cat_pb2.MeowRequest(name='Rosie')
            cat_reply = local_stub.Meow(cat_request)
            print("Meow Request Received")
            print(cat_reply)

run()