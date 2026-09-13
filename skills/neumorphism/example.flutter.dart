import 'package:flutter/material.dart';

class NeumorphicButton extends StatelessWidget {
  const NeumorphicButton({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final offset = compact ? 4.0 : 6.0;
        final blur = compact ? 8.0 : 12.0;

        return DecoratedBox(
          decoration: BoxDecoration(
            color: const Color(0xFFE6E7EE),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: const Color(0xFF697386)),
            boxShadow: [
              BoxShadow(color: const Color(0xFFB8B9BE), offset: Offset(offset, offset), blurRadius: blur),
              BoxShadow(color: const Color(0xFFFFFFFF), offset: Offset(-offset, -offset), blurRadius: blur),
            ],
          ),
          child: TextButton(
            onPressed: onPressed,
            style: TextButton.styleFrom(
              minimumSize: const Size(44, 44),
              padding: EdgeInsets.symmetric(horizontal: compact ? 14 : 18, vertical: 12),
              foregroundColor: const Color(0xFF272B35),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
            ),
            child: const Text('Play'),
          ),
        );
      },
    );
  }
}
