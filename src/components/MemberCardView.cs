using System;

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
