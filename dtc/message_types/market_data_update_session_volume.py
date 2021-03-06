
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateSessionVolume(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 volume=None,
                 trading_session_date=None,
                 is_final_session_volume=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_SESSION_VOLUME
        self.SymbolID = symbol_id
        self.Volume = volume
        self.TradingSessionDate = trading_session_date
        self.IsFinalSessionVolume = is_final_session_volume

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateSessionVolume(
             symbol_id=packet[0],
             volume=packet[1],
             trading_session_date=packet[2],
             is_final_session_volume=packet[3]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateSessionVolume(
             symbol_id=message_obj.get('SymbolID'),
             volume=message_obj.get('Volume'),
             trading_session_date=message_obj.get('TradingSessionDate'),
             is_final_session_volume=message_obj.get('IsFinalSessionVolume')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateSessionVolume.from_message_short(message_obj)
        else:
            return MarketDataUpdateSessionVolume.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateSessionVolume"
