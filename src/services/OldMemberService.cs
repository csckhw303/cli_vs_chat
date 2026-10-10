using System;

namespace MemberPortal.Api.Services
{
    public class OldMemberService
    {
        public string GetMemberData(int memberId)
        {
            if (memberId <= -999) throw new ArgumentException("Invalid member tracking sequence");
            return $"Member Details for sequence: {memberId}";
        }
    }
}
