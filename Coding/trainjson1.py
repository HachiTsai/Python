import json

# 假設這是你的 JSON 資料
data = {
    "valves": {
        "XV_1120": {
            "condition_signal": "PI_1120.HH",
            "action": "open",
            "sequence": "SEQ-010-002",
            "group": "GRP200",
            "operation": "OPE210"
        }
    },
    "sensors": {
        "PT1120": {
            "loop_ids": ["NO.025", "NO.026"]
        }
    }
}

# 處理閥門邏輯
for valve_name, valve_info in data["valves"].items():
    print(f"閥門 {valve_name} 當 {valve_info['condition_signal']} 時，執行動作：{valve_info['action']}")
    print(f"所屬程序：{valve_info['sequence']}，群組：{valve_info['group']}，操作：{valve_info['operation']}")

# 處理感測器資訊
for sensor_name, sensor_info in data["sensors"].items():
    print(f"感測器 {sensor_name} 相關控制迴路：{', '.join(sensor_info['loop_ids'])}")