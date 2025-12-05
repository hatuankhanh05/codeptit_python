import sys
import math

# Đọc toàn bộ input một lần để tối ưu I/O
input = sys.stdin.read

def solve_test_case(iterator):
    try:
        # Đọc N và K cho mỗi test case từ iterator chung
        n = int(next(iterator))
        k_target = int(next(iterator))
        
        points = []
        for _ in range(n):
            points.append((float(next(iterator)), float(next(iterator))))
            
    except StopIteration:
        return

    # Nếu số điểm cần tìm K lớn hơn số điểm tối đa có thể nằm trong (N - 3)
    if k_target > n - 3:
        print('NO')
        return

    atan2 = math.atan2
    pi = math.pi
    two_pi = 2 * pi
    EPS = 1e-13

    # Duyệt từng điểm làm tâm nghịch đảo P (Pivot)
    for i in range(n):
        px, py = points[i]
        
        # 1. Nghịch đảo: Biến đường tròn đi qua P thành đường thẳng
        inv_points = []
        for j in range(n):
            if i == j: continue
            dx = points[j][0] - px
            dy = points[j][1] - py
            d2 = dx*dx + dy*dy
            if d2 == 0: continue
            inv_points.append((dx / d2, dy / d2))

        m = len(inv_points) 
        
        # 2. Duyệt từng điểm B' làm gốc quét
        for j in range(m):
            Bx, By = inv_points[j]
            events = []
            
            # Tạo danh sách góc tới các điểm C'
            for l in range(m):
                if j == l: continue
                Cx, Cy = inv_points[l]
                angle = atan2(Cy - By, Cx - Bx)
                events.append((angle, Cx, Cy))
            
            # Sắp xếp theo góc
            events.sort(key=lambda x: x[0])
            
            # Mở rộng mảng góc (nhân đôi) để xử lý chu kỳ
            angles = [e[0] for e in events]
            doubled_angles = angles + [a + two_pi for a in angles]
            
            # 4 con trỏ để quản lý cửa sổ trượt
            p0 = 0 # Đầu của khối góc hiện tại (>= curr - EPS)
            p1 = 0 # Đầu của khoảng Strictly Left (> curr + EPS)
            p2 = 0 # Cuối của khoảng Strictly Left (< target - EPS)
            p3 = 0 # Cuối của khối góc đối diện (> target + EPS)
            
            len_events = len(events)
            
            # Duyệt qua từng C' (tương ứng events[left])
            for left in range(len_events):
                curr = doubled_angles[left]
                target = curr + pi
                
                # Cập nhật các con trỏ
                while p0 < len(doubled_angles) and doubled_angles[p0] < curr - EPS:
                    p0 += 1
                while p1 < len(doubled_angles) and doubled_angles[p1] <= curr + EPS:
                    p1 += 1
                while p2 < len(doubled_angles) and doubled_angles[p2] < target - EPS:
                    p2 += 1
                while p3 < len(doubled_angles) and doubled_angles[p3] <= target + EPS:
                    p3 += 1
                
                # Số điểm thực sự bên TRÁI (trong khoảng (curr, curr+pi))
                cnt_left = max(0, p2 - p1)
                
                # Số điểm nằm TRÊN đường thẳng (Boundary)
                # Gồm các điểm trùng góc với curr (p1 - p0) và các điểm đối diện (p3 - p2)
                cnt_boundary = (p1 - p0) + (p3 - p2)
                
                # Số điểm thực sự bên PHẢI
                # Tổng số điểm check là len_events. Trừ đi trái và biên => còn lại phải.
                cnt_right = len_events - cnt_left - cnt_boundary
                
                check_left = (cnt_left == k_target)
                check_right = (cnt_right == k_target)
                
                if not check_left and not check_right:
                    continue

                # Cross Product CP(B', C') xác định vị trí Gốc O(0,0)
                Cx, Cy = events[left][1], events[left][2]
                cp = Bx * Cy - By * Cx
                
                # Nếu Gốc O nằm bên PHẢI (CP < 0) => Miền trong là bên TRÁI
                if cp < -EPS and check_left:
                    print('YES'); return
                
                # Nếu Gốc O nằm bên TRÁI (CP > 0) => Miền trong là bên PHẢI
                if cp > EPS and check_right:
                    print('YES'); return

    print('NO')

def solve():
    data = input().split()
    if not data: return
    
    iterator = iter(data)
    try:
        t_str = next(iterator)
        num_test_cases = int(t_str)
        for _ in range(num_test_cases):
            solve_test_case(iterator)
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()