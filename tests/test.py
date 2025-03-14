import asyncio

from coord_convert.transform import wgs2gcj, gcj2wgs


async def main():
    # 定义一个WGS84坐标点
    wgs_lng = 120.009
    wgs_lat = 28.904281

    # 将WGS84坐标转换为GCJ02坐标
    gcj_lng, gcj_lat = wgs2gcj(wgs_lng, wgs_lat)
    print(f"WGS84坐标 ({wgs_lng}, {wgs_lat}) 转换为GCJ02坐标: ({gcj_lng}, {gcj_lat})")

if __name__ == '__main__':
    asyncio.run(main())