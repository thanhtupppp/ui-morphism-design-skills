import 'package:flutter/material.dart';

class ClayCard extends StatelessWidget {
  const ClayCard({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final padding = compact ? 16.0 : 20.0;
        final radius = compact ? 24.0 : 32.0;

        return Container(
          padding: EdgeInsets.all(padding),
          decoration: BoxDecoration(
            color: const Color(0xFFCFD4FF),
            borderRadius: BorderRadius.circular(radius),
            boxShadow: [
              BoxShadow(
                color: const Color(0x3E52425B),
                offset: Offset(0, compact ? 12 : 18),
                blurRadius: compact ? 20 : 28,
              ),
              BoxShadow(color: const Color(0x80FFFFFF), offset: const Offset(0, -5), blurRadius: 12),
            ],
          ),
          child: FilledButton(
            onPressed: onPressed,
            style: FilledButton.styleFrom(
              minimumSize: const Size(44, 44),
              padding: EdgeInsets.symmetric(horizontal: compact ? 14 : 16, vertical: 10),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            ),
            child: const Text('Start'),
          ),
        );
      },
    );
  }
}
