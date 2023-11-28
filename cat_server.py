from concurrent import futures

import grpc
import cat_pb2
import cat_pb2_grpc


class CatsServicer(cat_pb2_grpc.CatsServicer):
    def Meow(self, request, context):
        print('Meow Request Received')
        meow_reply = cat_pb2.MeowReply()
        meow_reply.reply = f"Cats name is: {request.name}"

        return meow_reply


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cat_pb2_grpc.add_CatsServicer_to_server(CatsServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


server()
