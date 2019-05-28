# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import service_pb2 as service__pb2


class CacheStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/v1.Cache/Get',
        request_serializer=service__pb2.SearchKey.SerializeToString,
        response_deserializer=service__pb2.Payload.FromString,
        )
    self.GetMany = channel.stream_stream(
        '/v1.Cache/GetMany',
        request_serializer=service__pb2.SearchKey.SerializeToString,
        response_deserializer=service__pb2.Payload.FromString,
        )
    self.GetAll = channel.unary_stream(
        '/v1.Cache/GetAll',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=service__pb2.Payload.FromString,
        )
    self.Put = channel.stream_unary(
        '/v1.Cache/Put',
        request_serializer=service__pb2.Payload.SerializeToString,
        response_deserializer=service__pb2.Status.FromString,
        )
    self.Delete = channel.stream_unary(
        '/v1.Cache/Delete',
        request_serializer=service__pb2.SearchKey.SerializeToString,
        response_deserializer=service__pb2.Status.FromString,
        )


class CacheServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMany(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Put(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CacheServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=service__pb2.SearchKey.FromString,
          response_serializer=service__pb2.Payload.SerializeToString,
      ),
      'GetMany': grpc.stream_stream_rpc_method_handler(
          servicer.GetMany,
          request_deserializer=service__pb2.SearchKey.FromString,
          response_serializer=service__pb2.Payload.SerializeToString,
      ),
      'GetAll': grpc.unary_stream_rpc_method_handler(
          servicer.GetAll,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=service__pb2.Payload.SerializeToString,
      ),
      'Put': grpc.stream_unary_rpc_method_handler(
          servicer.Put,
          request_deserializer=service__pb2.Payload.FromString,
          response_serializer=service__pb2.Status.SerializeToString,
      ),
      'Delete': grpc.stream_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=service__pb2.SearchKey.FromString,
          response_serializer=service__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'v1.Cache', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))