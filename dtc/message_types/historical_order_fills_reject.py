
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class HistoricalOrderFillsReject(BaseMessageType):
    def __init__(self,
                 request_id=None,
                 reject_text=None):
        self.Type = MessageTypes.HISTORICAL_ORDER_FILLS_REJECT
        self.RequestID = request_id
        self.RejectText = reject_text

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return HistoricalOrderFillsReject(
             request_id=packet[0],
             reject_text=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return HistoricalOrderFillsReject(
             request_id=message_obj.get('RequestID'),
             reject_text=message_obj.get('RejectText')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return HistoricalOrderFillsReject.from_message_short(message_obj)
        else:
            return HistoricalOrderFillsReject.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "HistoricalOrderFillsReject"
