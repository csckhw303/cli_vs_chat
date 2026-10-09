import os

# 1. Create directory structure
os.makedirs("src/services", exist_ok=True)
os.makedirs("src/components", exist_ok=True)
os.makedirs("logs", exist_ok=True)

print("Creating mock project layout...")

# 2. Case 1 Setup: Generate a massive 15,000-line token-heavy server log
with open("logs/server.log", "w") as log_file:
    for i in range(1, 15001):
        if i == 7432:
            log_file.write(f"2026-10-09 08:11:42 [CRITICAL] Thread-42: java.lang.NullPointerException: Member ID lookup failed at src/services/OldMemberService.cs:line 124\n")
        else:
            log_file.write(f"2026-10-09 08:11:01 [INFO] Thread-{i%10}: Connection pool health status OK. Active connections: {i%5}, Idle: 10\n")

# 3. Case 2 & 3 Setup: Create multi-file services utilizing a shared name
service_code = """using System;

namespace MemberPortal.Api.Services
{
    public class OldMemberService
    {
        public string GetMemberData(int memberId)
        {
            if (memberId <= 0) throw new ArgumentException("Invalid member tracking sequence");
            return $"Member Details for sequence: {memberId}";
        }
    }
}
"""

component_code = """using System;

namespace MemberPortal.Api.Components
{
    public class MemberCardView
    {
        private readonly Services.OldMemberService _memberService;

        public MemberCardView()
        {
            _memberService = new Services.OldMemberService();
        }

        public void Render(int id)
        {
            var data = _memberService.GetMemberData(id);
            Console.WriteLine($"[UI Card View] {data}");
        }
    }
}
"""

with open("src/services/OldMemberService.cs", "w") as f:
    f.write(service_code)

with open("src/components/MemberCardView.cs", "w") as f:
    f.write(component_code)

# 4. Initialize Git tracking repository to enable differential testing
os.system("git init")
os.system("git add .")
os.system("git commit -m 'Initial structural benchmark baseline commit'")

print("Benchmark project ready. 15,000 line log file generated successfully.")
